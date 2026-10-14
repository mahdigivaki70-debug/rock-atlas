package ir.rockatlas.data

import kotlinx.serialization.Serializable

@Serializable
data class SeedFile(
    val version: Int,
    val types: List<SeedType>,
    val stones: List<SeedStone>,
)

@Serializable
data class SeedType(
    val id: String,
    val nameFa: String,
    val nameEn: String,
    val description: String,
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
    val aliases: String,
    val typeId: String,
    val color: String,
    val pattern: String,
    val region: String,
    val country: String,
    val finishes: String,
    val uses: String,
    val description: String,
    val wikiTitle: String? = null,
)
