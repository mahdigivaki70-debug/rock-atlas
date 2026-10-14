package ir.rockatlas.identify

import ir.rockatlas.data.Stone
import ir.rockatlas.data.StoneType

enum class Answer { UNKNOWN, YES, NO }

/** Simple tests anyone can do on a stone in a shop or on site. */
data class FieldTests(
    /** "strong", "weak", "none" or null when not tested (a drop of vinegar or dilute acid). */
    val acid: String? = null,
    val pores: Answer = Answer.UNKNOWN,
    val translucent: Answer = Answer.UNKNOWN,
    val sparklyGrains: Answer = Answer.UNKNOWN,
    val veins: Answer = Answer.UNKNOWN,
) {
    val anyGiven: Boolean
        get() = acid != null || listOf(pores, translucent, sparklyGrains, veins).any { it != Answer.UNKNOWN }
}

data class Match(val stone: Stone, val score: Float)

/**
 * Ranks catalogue stones against a photo. Combines (a) colour and texture of
 * the photo, (b) optional field tests, and (c) an optional TFLite model.
 */
object Identifier {
    fun rank(
        features: ImageFeatures,
        tests: FieldTests,
        stones: List<Stone>,
        types: Map<String, StoneType>,
        model: Map<String, Float>?,
        limit: Int = 10,
    ): List<Match> {
        val maxColor = features.colors.values.maxOrNull()?.coerceAtLeast(1e-6f) ?: 1f
        val scored = stones.map { s ->
            val type = types[s.typeId]
            val color = (features.colors[s.color] ?: 0f) / maxColor
            val texture = textureFit(s.pattern, features.edgeDensity)
            var visual = if (tests.anyGiven) 0.6f * color + 0.15f * texture + 0.25f * testFit(s, type, tests)
            else 0.8f * color + 0.2f * texture
            if (model != null) {
                val p = maxOf(model[s.id] ?: 0f, model[s.typeId] ?: 0f)
                visual = 0.4f * visual + 0.6f * p
            }
            Match(s, visual.coerceIn(0f, 1f))
        }
        return scored.sortedByDescending { it.score }.take(limit)
    }

    private fun textureFit(pattern: String, edges: Float): Float = when (pattern) {
        "grain" -> (edges / 0.30f).coerceAtMost(1f)
        "uni" -> (1f - edges / 0.15f).coerceAtLeast(0f)
        "pore", "band", "vein", "cloud" -> 1f - kotlin.math.abs(edges - 0.12f) / 0.3f
        else -> 0.5f
    }.coerceIn(0f, 1f)

    private fun testFit(s: Stone, type: StoneType?, t: FieldTests): Float {
        val parts = mutableListOf<Float>()
        if (t.acid != null && type != null) {
            parts += when {
                t.acid == type.acid -> 1f
                t.acid != "none" && type.acid != "none" -> 0.5f
                else -> 0f
            }
        }
        fun yesNo(a: Answer, matches: Boolean) {
            if (a == Answer.YES) parts += if (matches) 1f else 0.15f
            if (a == Answer.NO) parts += if (matches) 0.3f else 1f
        }
        yesNo(t.pores, s.pattern == "pore" || s.typeId == "travertine")
        yesNo(t.translucent, s.typeId == "onyx")
        yesNo(t.sparklyGrains, s.pattern == "grain" || s.typeId == "granite" || s.typeId == "dolomitic")
        yesNo(t.veins, s.pattern == "vein" || s.pattern == "band")
        return if (parts.isEmpty()) 0.5f else parts.average().toFloat()
    }
}
