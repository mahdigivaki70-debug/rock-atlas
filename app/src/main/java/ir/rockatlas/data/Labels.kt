package ir.rockatlas.data

import androidx.compose.ui.graphics.Color

data class ColorFamily(val code: String, val fa: String, val swatch: Color)

/** Persian labels for the codes used in seed.json. */
object Labels {
    val colors: List<ColorFamily> = listOf(
        ColorFamily("wh", "سفید", Color(0xFFF2F0EA)),
        ColorFamily("cr", "کرم و بژ", Color(0xFFE3D2AE)),
        ColorFamily("ye", "زرد و لیمویی", Color(0xFFE0BE58)),
        ColorFamily("bn", "قهوه‌ای و گردویی", Color(0xFF85593A)),
        ColorFamily("rd", "قرمز", Color(0xFFA5432F)),
        ColorFamily("pk", "صورتی", Color(0xFFD7A09B)),
        ColorFamily("gn", "سبز", Color(0xFF3F6B4A)),
        ColorFamily("bl", "آبی", Color(0xFF4C6E92)),
        ColorFamily("pu", "بنفش", Color(0xFF6D5378)),
        ColorFamily("gy", "خاکستری", Color(0xFF8D9095)),
        ColorFamily("bk", "مشکی", Color(0xFF1F1F1F)),
    )
    private val colorByCode = colors.associateBy { it.code }
    fun color(code: String): ColorFamily = colorByCode[code] ?: colors.first()

    val patterns = linkedMapOf(
        "vein" to "رگه‌دار",
        "cloud" to "ابری",
        "uni" to "یکنواخت",
        "grain" to "دانه‌ای / خال‌دار",
        "pore" to "حفره‌دار",
        "band" to "نواری / لایه‌ای",
    )

    val finishes = linkedMapOf(
        "pol" to "صیقلی (پولیش)",
        "hon" to "مات (هونِد)",
        "fil" to "فیلرشده",
        "tum" to "آنتیک (تامبل)",
        "lea" to "چرمی (لِدر)",
        "fla" to "حرارتی (فلیم)",
        "bus" to "چکشی (بوش‌همر)",
        "san" to "سندبلاست",
        "spl" to "تیشه‌ای / طبیعی",
    )

    val uses = linkedMapOf(
        "fl" to "کف داخلی",
        "wl" to "دیوار داخلی",
        "fa" to "نمای خارجی",
        "pv" to "کف‌پوش محوطه",
        "st" to "پله",
        "ct" to "صفحهٔ کابینت",
        "bl" to "بک‌لایت (نور از پشت)",
        "rf" to "پوشش بام",
        "mo" to "مجسمه و تزئینات",
    )

    val acid = mapOf(
        "strong" to "می‌جوشد (کربناتی)",
        "weak" to "ضعیف، فقط پودر آن",
        "none" to "واکنش ندارد",
    )

    fun codes(csv: String): List<String> = csv.split(',').map { it.trim() }.filter { it.isNotEmpty() }
}
