package ir.rockatlas.identify

import android.content.Context
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.graphics.Matrix
import android.net.Uri
import androidx.core.content.FileProvider
import androidx.exifinterface.media.ExifInterface
import java.io.File
import java.util.UUID

/**
 * Safe image handling for photos coming from the camera or gallery:
 * size-checked, down-sampled while decoding, and re-encoded as a fresh JPEG
 * so EXIF metadata (GPS location, device info) never leaves the app.
 */
object ImageIO {
    private const val MAX_INPUT_BYTES = 40L * 1024 * 1024
    private const val MAX_EDGE = 1280

    fun captureDir(context: Context): File =
        File(context.cacheDir, "captures").apply { mkdirs() }

    /** A fresh, app-private target for the camera app to write into. */
    fun newCaptureUri(context: Context): Uri {
        val file = File(captureDir(context), "cam_${UUID.randomUUID()}.jpg")
        return FileProvider.getUriForFile(context, "${context.packageName}.fileprovider", file)
    }

    /** Decodes [source], strips metadata and stores a clean copy. Returns null on bad input. */
    fun importImage(context: Context, source: Uri): Pair<Bitmap, Uri>? = runCatching {
        val resolver = context.contentResolver
        val type = resolver.getType(source)
        if (type != null && !type.startsWith("image/")) return null
        resolver.openAssetFileDescriptor(source, "r")?.use { fd ->
            if (fd.length > MAX_INPUT_BYTES) return null
        }
        val bounds = BitmapFactory.Options().apply { inJustDecodeBounds = true }
        resolver.openInputStream(source)?.use { BitmapFactory.decodeStream(it, null, bounds) }
        if (bounds.outWidth <= 0 || bounds.outHeight <= 0) return null
        var sample = 1
        while (maxOf(bounds.outWidth, bounds.outHeight) / (sample * 2) >= MAX_EDGE) sample *= 2
        val opts = BitmapFactory.Options().apply { inSampleSize = sample }
        var bmp = resolver.openInputStream(source)?.use { BitmapFactory.decodeStream(it, null, opts) }
            ?: return null
        val rotation = resolver.openInputStream(source)?.use {
            when (ExifInterface(it).getAttributeInt(ExifInterface.TAG_ORIENTATION, ExifInterface.ORIENTATION_NORMAL)) {
                ExifInterface.ORIENTATION_ROTATE_90 -> 90f
                ExifInterface.ORIENTATION_ROTATE_180 -> 180f
                ExifInterface.ORIENTATION_ROTATE_270 -> 270f
                else -> 0f
            }
        } ?: 0f
        if (rotation != 0f) {
            bmp = Bitmap.createBitmap(bmp, 0, 0, bmp.width, bmp.height, Matrix().apply { postRotate(rotation) }, true)
        }
        val scale = MAX_EDGE.toFloat() / maxOf(bmp.width, bmp.height)
        if (scale < 1f) {
            bmp = Bitmap.createScaledBitmap(bmp, (bmp.width * scale).toInt(), (bmp.height * scale).toInt(), true)
        }
        val out = File(captureDir(context), "img_${UUID.randomUUID()}.jpg")
        out.outputStream().use { bmp.compress(Bitmap.CompressFormat.JPEG, 90, it) }
        bmp to FileProvider.getUriForFile(context, "${context.packageName}.fileprovider", out)
    }.getOrNull()

    /** Removes old captures so the cache does not grow forever. */
    fun cleanup(context: Context, keep: Uri?) {
        val keepName = keep?.lastPathSegment
        captureDir(context).listFiles()?.forEach { f ->
            if (f.name != keepName && System.currentTimeMillis() - f.lastModified() > 60_000) f.delete()
        }
    }
}
