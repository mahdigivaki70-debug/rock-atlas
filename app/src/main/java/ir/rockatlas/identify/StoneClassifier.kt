package ir.rockatlas.identify

import android.content.Context
import android.graphics.Bitmap
import org.tensorflow.lite.DataType
import org.tensorflow.lite.Interpreter
import java.io.FileInputStream
import java.nio.ByteBuffer
import java.nio.ByteOrder
import java.nio.MappedByteBuffer
import java.nio.channels.FileChannel

/**
 * Optional on-device image classifier. Drop a TensorFlow Lite model at
 * assets/stone_model.tflite with labels in assets/stone_labels.txt (one stone id
 * or stone type id per line, in output order) and it is used automatically.
 * tools/train_model.py produces a compatible model from a folder of photos.
 */
class StoneClassifier private constructor(
    private val interpreter: Interpreter,
    val labels: List<String>,
) {
    private val inShape = interpreter.getInputTensor(0).shape() // [1, h, w, 3]
    private val inType = interpreter.getInputTensor(0).dataType()
    private val outType = interpreter.getOutputTensor(0).dataType()

    /** Returns label -> probability. */
    @Synchronized
    fun classify(bitmap: Bitmap): Map<String, Float> {
        val h = inShape[1]
        val w = inShape[2]
        val scaled = Bitmap.createScaledBitmap(bitmap, w, h, true)
        val px = IntArray(w * h)
        scaled.getPixels(px, 0, w, 0, 0, w, h)
        val input = if (inType == DataType.UINT8) {
            ByteBuffer.allocateDirect(w * h * 3).apply {
                for (p in px) { put((p shr 16 and 0xFF).toByte()); put((p shr 8 and 0xFF).toByte()); put((p and 0xFF).toByte()) }
            }
        } else {
            // Float models are expected to include their own rescaling layer (raw 0..255 input).
            ByteBuffer.allocateDirect(w * h * 3 * 4).order(ByteOrder.nativeOrder()).apply {
                for (p in px) {
                    putFloat((p shr 16 and 0xFF).toFloat()); putFloat((p shr 8 and 0xFF).toFloat()); putFloat((p and 0xFF).toFloat())
                }
            }
        }
        input.rewind()
        val scores = FloatArray(labels.size)
        if (outType == DataType.UINT8) {
            val out = Array(1) { ByteArray(labels.size) }
            interpreter.run(input, out)
            for (i in scores.indices) scores[i] = (out[0][i].toInt() and 0xFF) / 255f
        } else {
            val out = Array(1) { FloatArray(labels.size) }
            interpreter.run(input, out)
            out[0].copyInto(scores)
        }
        return labels.indices.associate { labels[it] to scores[it] }
    }

    companion object {
        private const val MODEL = "stone_model.tflite"
        private const val LABELS = "stone_labels.txt"
        private val LABEL_RE = Regex("^[a-z0-9_]{1,64}$")

        /** Null when no model is bundled or it cannot be loaded. */
        fun load(context: Context): StoneClassifier? = runCatching {
            val assets = context.assets
            if (assets.list("")?.contains(MODEL) != true) return null
            val labels = assets.open(LABELS).bufferedReader().readLines()
                .map { it.trim() }.filter { it.matches(LABEL_RE) }
            val buffer: MappedByteBuffer = assets.openFd(MODEL).use { fd ->
                FileInputStream(fd.fileDescriptor).channel.use {
                    it.map(FileChannel.MapMode.READ_ONLY, fd.startOffset, fd.declaredLength)
                }
            }
            val interpreter = Interpreter(buffer, Interpreter.Options().setNumThreads(2))
            if (interpreter.getOutputTensor(0).shape().last() != labels.size) return null
            StoneClassifier(interpreter, labels)
        }.getOrNull()
    }
}
