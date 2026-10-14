package ir.rockatlas.data

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase

@Database(
    entities = [Category::class, StoneType::class, Stone::class, CachedImage::class, Favorite::class],
    version = 3,
    exportSchema = true,
)
abstract class AppDatabase : RoomDatabase() {
    abstract fun dao(): StoneDao

    companion object {
        fun create(context: Context): AppDatabase =
            Room.databaseBuilder(context, AppDatabase::class.java, "rock_atlas.db")
                // Catalogue tables are re-imported from assets on every schema change.
                .fallbackToDestructiveMigration()
                .build()
    }
}
