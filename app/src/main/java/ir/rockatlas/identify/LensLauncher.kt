package ir.rockatlas.identify

import android.content.ActivityNotFoundException
import android.content.ClipData
import android.content.Context
import android.content.Intent
import android.net.Uri

/**
 * Google Lens has no public API, so the app hands the photo to the Lens app
 * (or the Google app, which contains Lens) and the user brings the name back
 * to search the atlas. Only a metadata-free copy of the photo is shared.
 */
object LensLauncher {
    private val packages = listOf("com.google.ar.lens", "com.google.android.googlequicksearchbox")

    fun open(context: Context, image: Uri): Boolean {
        for (pkg in packages) {
            try {
                context.startActivity(shareIntent(image).setPackage(pkg))
                return true
            } catch (e: ActivityNotFoundException) {
                // Try the next app.
            }
        }
        return try {
            context.startActivity(Intent.createChooser(shareIntent(image), null).addFlags(Intent.FLAG_ACTIVITY_NEW_TASK))
            true
        } catch (e: ActivityNotFoundException) {
            false
        }
    }

    private fun shareIntent(image: Uri) = Intent(Intent.ACTION_SEND).apply {
        type = "image/jpeg"
        putExtra(Intent.EXTRA_STREAM, image)
        clipData = ClipData.newRawUri(null, image)
        addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION or Intent.FLAG_ACTIVITY_NEW_TASK)
    }
}
