package ir.rockatlas.data

data class SearchFilters(
    val typeId: String? = null,
    val color: String? = null,
    val use: String? = null,
    val country: String? = null,
    val onlyFavorites: Boolean = false,
)

/** In-memory search: the catalogue is a few hundred rows, so this stays instant. */
object SearchEngine {
    /** Category names, set once categories load; used only for matching. */
    @Volatile
    var categoryNames: Map<String, String> = emptyMap()

    private fun categoryName(id: String?) = id?.let { categoryNames[it] }.orEmpty()

    fun search(
        query: String,
        filters: SearchFilters,
        stones: List<Stone>,
        types: Map<String, StoneType>,
        favorites: Set<String>,
    ): List<Stone> {
        val terms = TextNormalizer.normalize(TextNormalizer.cleanQuery(query))
            .split(' ').filter { it.isNotEmpty() }
        return stones.asSequence()
            .filter { filters.typeId == null || it.typeId == filters.typeId }
            .filter { filters.color == null || it.color == filters.color }
            .filter { filters.use == null || filters.use in Labels.codes(it.uses) }
            .filter { filters.country == null || it.country == filters.country }
            .filter { !filters.onlyFavorites || it.id in favorites }
            .mapNotNull { stone ->
                if (terms.isEmpty()) return@mapNotNull stone to 0
                val type = types[stone.typeId]
                // Every language is searched, so an English name works in the Persian UI too.
                val name = TextNormalizer.normalize(
                    "${stone.nameFa} ${stone.nameEn} ${stone.nameAr} ${stone.nameRu} ${stone.aliases}",
                )
                val rest = TextNormalizer.normalize(
                    listOf(
                        stone.region, stone.regionEn, stone.regionAr, stone.regionRu,
                        stone.country, stone.countryEn, stone.countryAr, stone.countryRu,
                        stone.description, stone.descEn,
                        type?.nameFa.orEmpty(), type?.nameEn.orEmpty(), type?.nameAr.orEmpty(), type?.nameRu.orEmpty(),
                        categoryName(type?.categoryId),
                        Labels.color(stone.color).label.all, Labels.patterns[stone.pattern]?.all.orEmpty(),
                    ).joinToString(" "),
                )
                var score = 0
                for (t in terms) {
                    score += when {
                        name.startsWith(t) -> 10
                        name.contains(t) -> 6
                        rest.contains(t) -> 2
                        else -> return@mapNotNull null
                    }
                }
                stone to score
            }
            .sortedWith(compareByDescending<Pair<Stone, Int>> { it.second }.thenBy { it.first.nameFa })
            .map { it.first }
            .toList()
    }
}
