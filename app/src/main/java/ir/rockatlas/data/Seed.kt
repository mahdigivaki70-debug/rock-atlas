package ir.rockatlas.data

import kotlinx.serialization.Serializable

@Serializable
data class SeedFile(
    val version: Int,
    val categories: List<SeedCategory>,
    val types: List<SeedType>,
    val stones: List<SeedStone>,
)

@Serializable
data class SeedCategory(
    val id: String,
    val nameFa: String,
    val nameEn: String,
    val nameAr: String,
    val nameRu: String,
    val sortOrder: Int,
)

@Serializable
data class SeedType(
    val id: String,
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
    val acid: String,
    val standard: String,
    val finishes: String,
    val uses: String,
    val wikiTitle: String,
    val sortOrder: Int,
)

@Serializable
data class SeedStone(
    val id: String,
    val nameFa: String,
    val nameEn: String,
    val nameAr: String,
    val nameRu: String,
    val aliases: String,
    val typeId: String,
    val color: String,
    val pattern: String,
    val region: String,
    val regionEn: String,
    val regionAr: String,
    val regionRu: String,
    val country: String,
    val countryEn: String,
    val countryAr: String,
    val countryRu: String,
    val finishes: String,
    val uses: String,
    val description: String,
    val descEn: String,
    val descAr: String,
    val descRu: String,
    val wikiTitle: String? = null,
)
