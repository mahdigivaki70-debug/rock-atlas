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
                val name = TextNormalizer.normalize("${stone.nameFa} ${stone.nameEn} ${stone.aliases}")
                val rest = TextNormalizer.normalize(
                    listOf(
                        stone.region, stone.country, stone.description,
                        type?.nameFa.orEmpty(), type?.nameEn.orEmpty(),
                        Labels.color(stone.color).fa, Labels.patterns[stone.pattern].orEmpty(),
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
