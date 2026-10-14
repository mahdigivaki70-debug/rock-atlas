package ir.rockatlas.data

import androidx.room.Entity
import androidx.room.Index
import androidx.room.PrimaryKey

/** Top-level grouping shown on the home screen (marble, granite, ...). */
@Entity(tableName = "categories")
data class Category(
    @PrimaryKey val id: String,
    val nameFa: String,
    val nameEn: String,
    val nameAr: String,
    val nameRu: String,
    val sortOrder: Int,
) {
    fun name(lang: Lang) = pick(lang, nameFa, nameEn, nameAr, nameRu)
}

/** Petrological type; lab property ranges live here. Subcategory of a [Category]. */
@Entity(tableName = "stone_types", indices = [Index("categoryId")])
data class StoneType(
    @PrimaryKey val id: String,
    val categoryId: String,
    val nameFa: String,
    val nameEn: String,
    val nameAr: String,
    val nameRu: String,
    val description: String,
    val descEn: String,
    val descAr: String,
    val descRu: String,
    val densityMin: Double,
    val densityMax: Double,
    val absorptionMin: Double,
    val absorptionMax: Double,
    val compressiveMin: Double,
    val compressiveMax: Double,
    val flexuralMin: Double,
    val flexuralMax: Double,
    val mohsMin: Double,
    val mohsMax: Double,
    /** strong / weak / none: reaction to cold dilute hydrochloric acid. */
    val acid: String,
    val standard: String,
    val finishes: String,
    val uses: String,
    val wikiTitle: String,
    val sortOrder: Int,
) {
    fun name(lang: Lang) = pick(lang, nameFa, nameEn, nameAr, nameRu)
    fun desc(lang: Lang) = pick(lang, description, descEn, descAr, descRu)
}

@Entity(tableName = "stones", indices = [Index("typeId")])
data class Stone(
    @PrimaryKey val id: String,
    val nameFa: String,
    val nameEn: String,
    val nameAr: String,
    val nameRu: String,
    val aliases: String,
    val typeId: String,
    val color: String,
    val pattern: String,
    /** Persian region / country are also the stable keys used by filters. */
    val region: String,
    val regionEn: String,
    val regionAr: String,
    val regionRu: String,
    val country: String,
    val countryEn: String,
    val countryAr: String,
    val countryRu: String,
    /** Comma-separated finish codes, see [Labels.finishes]. */
    val finishes: String,
    /** Comma-separated use codes, see [Labels.uses]. */
    val uses: String,
    val description: String,
    val descEn: String,
    val descAr: String,
    val descRu: String,
    val wikiTitle: String?,
    /** JSON of a [SeedLab] when the producer published measured values, else null. */
    val labJson: String?,
) {
    /** Producer-measured lab values; null means use the type's typical ranges. */
    fun lab(): SeedLab? = labJson?.let { runCatching { labFormat.decodeFromString(SeedLab.serializer(), it) }.getOrNull() }

    fun name(lang: Lang) = pick(lang, nameFa, nameEn, nameAr, nameRu)
    /** The name in the other script, shown under the main name. */
    fun subtitle(lang: Lang) = if (lang == Lang.EN) nameFa else nameEn
    fun region(lang: Lang) = pick(lang, region, regionEn, regionAr, regionRu)
    fun country(lang: Lang) = pick(lang, country, countryEn, countryAr, countryRu)
    fun desc(lang: Lang) = pick(lang, description, descEn, descAr, descRu)
    fun place(lang: Lang): String {
        val r = region(lang)
        val c = country(lang)
        return if (r == c) c else "$r${Strings.of(lang).comma}$c"
    }
}

/** Kept apart from [Stone] so re-importing the seed does not drop cached photos. */
@Entity(tableName = "image_cache")
data class CachedImage(
    @PrimaryKey val stoneId: String,
    /** HTTPS URL on upload.wikimedia.org, or empty when no free image was found. */
    val imageUrl: String,
    /** Commons file page with author and licence. */
    val filePageUrl: String,
    /** True when the photo shows the stone type in general, not this exact stone. */
    val generic: Boolean,
    val fetchedAt: Long,
)

@Entity(tableName = "favorites")
data class Favorite(@PrimaryKey val stoneId: String)

private val labFormat = kotlinx.serialization.json.Json { ignoreUnknownKeys = true }

internal fun pick(lang: Lang, fa: String, en: String, ar: String, ru: String) = when (lang) {
    Lang.FA -> fa
    Lang.EN -> en
    Lang.AR -> ar
    Lang.RU -> ru
}

fun SeedCategory.toEntity() = Category(id, nameFa, nameEn, nameAr, nameRu, sortOrder)

fun SeedType.toEntity() = StoneType(
    id, categoryId, nameFa, nameEn, nameAr, nameRu, description, descEn, descAr, descRu,
    densityMin, densityMax, absorptionMin, absorptionMax, compressiveMin, compressiveMax,
    flexuralMin, flexuralMax, mohsMin, mohsMax, acid, standard, finishes, uses, wikiTitle, sortOrder,
)

fun SeedStone.toEntity() = Stone(
    id, nameFa, nameEn, nameAr, nameRu, aliases, typeId, color, pattern,
    region, regionEn, regionAr, regionRu, country, countryEn, countryAr, countryRu,
    finishes, uses, description, descEn, descAr, descRu, wikiTitle,
    lab?.let { labFormat.encodeToString(SeedLab.serializer(), it) },
)
