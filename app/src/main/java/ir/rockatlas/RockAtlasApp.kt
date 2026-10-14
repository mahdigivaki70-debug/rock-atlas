package ir.rockatlas

import android.app.Application
import coil.ImageLoader
import coil.ImageLoaderFactory
import coil.disk.DiskCache
import ir.rockatlas.data.AppDatabase
import ir.rockatlas.data.Repository
import ir.rockatlas.data.WikiImageService
import okhttp3.OkHttpClient
import java.io.IOException
import java.util.concurrent.TimeUnit

class RockAtlasApp : Application(), ImageLoaderFactory {

    /** Wikimedia asks API clients to send a descriptive User-Agent. */
    val httpClient: OkHttpClient by lazy {
        OkHttpClient.Builder()
            .connectTimeout(10, TimeUnit.SECONDS)
            .readTimeout(15, TimeUnit.SECONDS)
            .followSslRedirects(false)
            .addInterceptor { chain ->
                val req = chain.request()
                // IOException (not IllegalArgumentException) so OkHttp fails the call instead of crashing.
                if (!req.url.isHttps || req.url.host !in ALLOWED_HOSTS) throw IOException("Blocked request to ${req.url.host}")
                chain.proceed(req.newBuilder().header("User-Agent", USER_AGENT).build())
            }
            .build()
    }

    val repository: Repository by lazy {
        Repository(this, AppDatabase.create(this), WikiImageService(httpClient))
    }

    override fun newImageLoader(): ImageLoader =
        ImageLoader.Builder(this)
            .okHttpClient(httpClient)
            .diskCache {
                DiskCache.Builder()
                    .directory(cacheDir.resolve("images"))
                    .maxSizeBytes(150L * 1024 * 1024)
                    .build()
            }
            .crossfade(true)
            .build()

    companion object {
        const val USER_AGENT = "RockAtlas/1.0 (Android building-stone atlas)"
        val ALLOWED_HOSTS = setOf("en.wikipedia.org", "upload.wikimedia.org")
    }
}
