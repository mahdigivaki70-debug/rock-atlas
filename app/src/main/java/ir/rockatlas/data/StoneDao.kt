package ir.rockatlas.data

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Transaction
import kotlinx.coroutines.flow.Flow

@Dao
interface StoneDao {
    @Query("SELECT * FROM stone_types ORDER BY sortOrder")
    fun types(): Flow<List<StoneType>>

    @Query("SELECT * FROM stones ORDER BY nameFa")
    fun stones(): Flow<List<Stone>>

    @Query("SELECT * FROM stones WHERE id = :id")
    fun stone(id: String): Flow<Stone?>

    @Query("SELECT * FROM stone_types WHERE id = :id")
    fun type(id: String): Flow<StoneType?>

    @Query("SELECT * FROM stone_types WHERE id = :id")
    suspend fun typeNow(id: String): StoneType?

    @Query("SELECT * FROM stones WHERE id = :id")
    suspend fun stoneNow(id: String): Stone?

    @Query("SELECT * FROM stones")
    suspend fun allStonesNow(): List<Stone>

    @Query("SELECT * FROM stone_types")
    suspend fun allTypesNow(): List<StoneType>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertTypes(types: List<StoneType>)

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertStones(stones: List<Stone>)

    @Query("DELETE FROM stones")
    suspend fun clearStones()

    @Query("DELETE FROM stone_types")
    suspend fun clearTypes()

    @Transaction
    suspend fun replaceSeed(types: List<StoneType>, stones: List<Stone>) {
        clearStones()
        clearTypes()
        insertTypes(types)
        insertStones(stones)
    }

    @Query("SELECT * FROM image_cache")
    fun images(): Flow<List<CachedImage>>

    @Query("SELECT * FROM image_cache WHERE stoneId = :id")
    suspend fun imageNow(id: String): CachedImage?

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun putImage(image: CachedImage)

    @Query("SELECT stoneId FROM favorites")
    fun favoriteIds(): Flow<List<String>>

    @Insert(onConflict = OnConflictStrategy.IGNORE)
    suspend fun addFavorite(f: Favorite)

    @Query("DELETE FROM favorites WHERE stoneId = :id")
    suspend fun removeFavorite(id: String)
}
