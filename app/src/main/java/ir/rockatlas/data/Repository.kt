package ir.rockatlas.data

import android.content.Context
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.sync.Semaphore
import kotlinx.coroutines.sync.withPermit
import kotlinx.coroutines.withContext
import kotlinx.serialization.json.Json
import java.util.Collections

class Repository(
    private val context: Context,
    private val db: AppDatabase,
    private val wiki: WikiImageService,
) {
    private val dao = db.dao()
    private val json = Json { ignoreUnknownKeys = true }
    private val prefs = context.getSharedPreferences("seed", Context.MODE_PRIVATE)
    private val imageGate = Semaphore(3)
    private val inFlight: MutableSet<String> = Collections.synchronizedSet(mutableSetOf())

    val categories: Flow<List<Category>> = dao.categories()
    val types: Flow<List<StoneType>> = dao.types()
    val stones: Flow<List<Stone>> = dao.stones()
    val favoriteIds: Flow<Set<String>> = dao.favoriteIds().map { it.toSet() }
    val images: Flow<Map<String, CachedImage>> = dao.images().map { list -> list.associateBy { it.stoneId } }

    fun stone(id: String) = dao.stone(id)
    fun type(id: String) = dao.type(id)

    /** Imports assets/seed.json when it is newer than what is installed. */
    suspend fun ensureSeeded() = withContext(Dispatchers.IO) {
        val text = context.assets.open("seed.json").bufferedReader(Charsets.UTF_8).use { it.readText() }
        val seed = json.decodeFromString(SeedFile.serializer(), text)
        // The count check covers a destructive schema migration that emptied the tables.
        if (prefs.getInt("version", 0) >= seed.version && dao.stoneCount() > 0) return@withContext
        dao.replaceSeed(
            seed.categories.map { it.toEntity() },
            seed.types.map { it.toEntity() },
            seed.stones.map { it.toEntity() },
        )
        prefs.edit().putInt("version", seed.version).apply()
    }

    suspend fun toggleFavorite(id: String, isFavorite: Boolean) {
        if (isFavorite) dao.removeFavorite(id) else dao.addFavorite(Favorite(id))
    }

    /** Looks up and caches a Commons photo for a stone, falling back to its type's article. */
    suspend fun ensureImage(stoneId: String) {
        val cached = dao.imageNow(stoneId)
        val now = System.currentTimeMillis()
        if (cached != null && (cached.imageUrl.isNotEmpty() || now - cached.fetchedAt < RETRY_MS)) return
        if (!inFlight.add(stoneId)) return
        try {
            imageGate.withPermit {
                val stone = dao.stoneNow(stoneId) ?: return
                // A producer photo from the seed wins over a Wikipedia lookup.
                stone.lab()?.imageUrl?.takeIf { it.startsWith(PRODUCER_IMAGE_PREFIX) }?.let { url ->
                    dao.putImage(CachedImage(stoneId, url, stone.lab()!!.sourceUrl, generic = false, fetchedAt = now))
                    return
                }
                val type = dao.typeNow(stone.typeId)
                val specific = stone.wikiTitle?.let { wiki.lookup(it) }
                val found = specific ?: type?.let { wiki.lookup(it.wikiTitle) }
                dao.putImage(
                    CachedImage(
                        stoneId = stoneId,
                        imageUrl = found?.imageUrl.orEmpty(),
                        filePageUrl = found?.filePageUrl.orEmpty(),
                        generic = specific == null,
                        fetchedAt = now,
                    ),
                )
            }
        } finally {
            inFlight.remove(stoneId)
        }
    }

    private companion object {
        const val PRODUCER_IMAGE_PREFIX = "https://nexstone.ir/"
        const val RETRY_MS = 3L * 24 * 60 * 60 * 1000
    }
}
