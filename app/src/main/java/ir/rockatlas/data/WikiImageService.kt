package ir.rockatlas.data

import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import kotlinx.serialization.json.Json
import kotlinx.serialization.json.JsonObject
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.intOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive
import okhttp3.HttpUrl
import okhttp3.OkHttpClient
import okhttp3.Request

data class WikiImage(val imageUrl: String, val filePageUrl: String)

/**
 * Finds a freely licensed photo for an article through the Wikipedia REST API.
 * Only images hosted on Wikimedia Commons are accepted (never locally hosted
 * non-free files), and every URL is checked to be HTTPS on a Wikimedia host.
 */
class WikiImageService(private val client: OkHttpClient) {
    private val json = Json { ignoreUnknownKeys = true }

    suspend fun lookup(title: String): WikiImage? = withContext(Dispatchers.IO) {
        val url = HttpUrl.Builder()
            .scheme("https")
            .host("en.wikipedia.org")
            .addPathSegments("api/rest_v1/page/summary")
            .addPathSegment(title.replace(' ', '_'))
            .build()
        val request = Request.Builder().url(url).header("Accept", "application/json").build()
        runCatching {
            client.newCall(request).execute().use { resp ->
                if (!resp.isSuccessful) return@use null
                val body = resp.body ?: return@use null
                if (body.contentLength() > MAX_BYTES) return@use null
                val text = body.source().let { src ->
                    src.request(MAX_BYTES + 1)
                    if (src.buffer.size > MAX_BYTES) return@use null
                    src.buffer.readUtf8()
                }
                parse(json.parseToJsonElement(text).jsonObject)
            }
        }.getOrNull()
    }

    private fun parse(root: JsonObject): WikiImage? {
        val original = root["originalimage"]?.jsonObject ?: return null
        val source = original["source"]?.jsonPrimitive?.contentOrNull ?: return null
        if (!isCommons(source)) return null
        val width = original["width"]?.jsonPrimitive?.intOrNull ?: 0
        val thumb = root["thumbnail"]?.jsonObject?.get("source")?.jsonPrimitive?.contentOrNull
        // Large originals are swapped for a 960px thumbnail to save data.
        val display = if (width > 960 && thumb != null && isCommons(thumb)) {
            thumb.replace(Regex("/\\d+px-"), "/960px-")
        } else {
            source
        }
        val fileName = source.substringAfterLast('/')
        return WikiImage(display, "https://commons.wikimedia.org/wiki/File:$fileName")
    }

    private fun isCommons(url: String): Boolean =
        url.startsWith("https://upload.wikimedia.org/wikipedia/commons/")

    private companion object {
        const val MAX_BYTES = 256L * 1024
    }
}
