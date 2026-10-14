package ir.rockatlas.data

import androidx.room.Entity
import androidx.room.Index
import androidx.room.PrimaryKey

@Entity(tableName = "stone_types")
data class StoneType(
    @PrimaryKey val id: String,
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
    /** strong / weak / none: reaction to cold dilute hydrochloric acid. */
    val acid: String,
    val standard: String,
    val finishes: String,
    val uses: String,
    val wikiTitle: String,
    val sortOrder: Int,
)

@Entity(tableName = "stones", indices = [Index("typeId")])
data class Stone(
    @PrimaryKey val id: String,
    val nameFa: String,
    val nameEn: String,
    val aliases: String,
    val typeId: String,
    val color: String,
    val pattern: String,
    val region: String,
    val country: String,
    /** Comma-separated finish codes, see [Labels.finishes]. */
    val finishes: String,
    /** Comma-separated use codes, see [Labels.uses]. */
    val uses: String,
    val description: String,
    val wikiTitle: String?,
)

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

fun SeedType.toEntity() = StoneType(
    id, nameFa, nameEn, description, densityMin, densityMax, absorptionMin, absorptionMax,
    compressiveMin, compressiveMax, flexuralMin, flexuralMax, mohsMin, mohsMax, acid, standard,
    finishes, uses, wikiTitle, sortOrder,
)

fun SeedStone.toEntity() = Stone(
    id, nameFa, nameEn, aliases, typeId, color, pattern, region, country, finishes, uses,
    description, wikiTitle,
)
