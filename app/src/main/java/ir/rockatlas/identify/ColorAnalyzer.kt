package ir.rockatlas.identify

import android.graphics.Bitmap
import android.graphics.Color
import androidx.compose.ui.graphics.toArgb
import ir.rockatlas.data.Labels
import kotlin.math.abs
import kotlin.math.cbrt
import kotlin.math.exp
import kotlin.math.pow

data class ImageFeatures(
    /** Share of the photo attributed to each colour family code (sums to 1). */
    val colors: Map<String, Float>,
    /** 0..1, share of strong edges: high for speckled granite, low for plain stone. */
    val edgeDensity: Float,
)

/** Hand-written colour and texture features; works with no model and no network. */
object ColorAnalyzer {
    private const val SIZE = 96
    private val swatchLab: List<Pair<String, FloatArray>> =
        Labels.colors.map { it.code to rgbToLab(it.swatch.toArgb()) }

    fun analyze(bitmap: Bitmap): ImageFeatures {
        // Use the central 70% of the frame, where the stone usually is.
        val cx = (bitmap.width * 0.15f).toInt()
        val cy = (bitmap.height * 0.15f).toInt()
        val crop = Bitmap.createBitmap(bitmap, cx, cy, bitmap.width - 2 * cx, bitmap.height - 2 * cy)
        val small = Bitmap.createScaledBitmap(crop, SIZE, SIZE, true)
        val px = IntArray(SIZE * SIZE)
        small.getPixels(px, 0, SIZE, 0, 0, SIZE, SIZE)

        val hist = HashMap<String, Float>()
        val gray = FloatArray(px.size)
        for ((i, p) in px.withIndex()) {
            val lab = rgbToLab(p)
            gray[i] = lab[0]
            // Soft assignment: nearby families share the pixel.
            val weights = swatchLab.map { (code, s) -> code to exp(-dist2(lab, s) / 400f) }
            val total = weights.sumOf { it.second.toDouble() }.toFloat().coerceAtLeast(1e-6f)
            for ((code, w) in weights) hist[code] = (hist[code] ?: 0f) + w / total
        }
        val n = px.size.toFloat()
        val colors = hist.mapValues { it.value / n }

        var edges = 0
        for (y in 1 until SIZE - 1) for (x in 1 until SIZE - 1) {
            val i = y * SIZE + x
            val g = abs(gray[i + 1] - gray[i - 1]) + abs(gray[i + SIZE] - gray[i - SIZE])
            if (g > 18f) edges++
        }
        return ImageFeatures(colors, edges / ((SIZE - 2f) * (SIZE - 2f)))
    }

    private fun dist2(a: FloatArray, b: FloatArray): Float {
        // Lightness differences matter a little less than hue for stone colour.
        val dl = (a[0] - b[0]) * 0.7f
        val da = a[1] - b[1]
        val db = a[2] - b[2]
        return dl * dl + da * da + db * db
    }

    private fun rgbToLab(c: Int): FloatArray {
        fun lin(v: Int): Double { val s = v / 255.0; return if (s <= 0.04045) s / 12.92 else ((s + 0.055) / 1.055).pow(2.4) }
        val r = lin(Color.red(c)); val g = lin(Color.green(c)); val b = lin(Color.blue(c))
        val x = (r * 0.4124 + g * 0.3576 + b * 0.1805) / 0.95047
        val y = r * 0.2126 + g * 0.7152 + b * 0.0722
        val z = (r * 0.0193 + g * 0.1192 + b * 0.9505) / 1.08883
        fun f(t: Double) = if (t > 0.008856) cbrt(t) else 7.787 * t + 16.0 / 116
        val fx = f(x); val fy = f(y); val fz = f(z)
        return floatArrayOf((116 * fy - 16).toFloat(), (500 * (fx - fy)).toFloat(), (200 * (fy - fz)).toFloat())
    }
}
