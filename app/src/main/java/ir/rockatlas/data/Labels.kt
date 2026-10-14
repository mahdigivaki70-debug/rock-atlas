package ir.rockatlas.data

import androidx.compose.ui.graphics.Color

/** A label in fa, en, ar, ru. */
data class L(val fa: String, val en: String, val ar: String, val ru: String) {
    operator fun get(lang: Lang) = pick(lang, fa, en, ar, ru)
    val all: String get() = "$fa $en $ar $ru"
}

data class ColorFamily(val code: String, val label: L, val swatch: Color) {
    fun name(lang: Lang) = label[lang]
}

/** Localised labels for the codes used in seed.json. */
object Labels {
    val colors: List<ColorFamily> = listOf(
        ColorFamily("wh", L("سفید", "White", "أبيض", "Белый"), Color(0xFFF2F0EA)),
        ColorFamily("cr", L("کرم و بژ", "Cream & beige", "كريمي وبيج", "Кремовый и бежевый"), Color(0xFFE3D2AE)),
        ColorFamily("ye", L("زرد و لیمویی", "Yellow & gold", "أصفر وذهبي", "Жёлтый и золотой"), Color(0xFFE0BE58)),
        ColorFamily("bn", L("قهوه‌ای و گردویی", "Brown & walnut", "بني وجوزي", "Коричневый и ореховый"), Color(0xFF85593A)),
        ColorFamily("rd", L("قرمز", "Red", "أحمر", "Красный"), Color(0xFFA5432F)),
        ColorFamily("pk", L("صورتی", "Pink", "وردي", "Розовый"), Color(0xFFD7A09B)),
        ColorFamily("gn", L("سبز", "Green", "أخضر", "Зелёный"), Color(0xFF3F6B4A)),
        ColorFamily("bl", L("آبی", "Blue", "أزرق", "Синий"), Color(0xFF4C6E92)),
        ColorFamily("pu", L("بنفش", "Purple", "بنفسجي", "Фиолетовый"), Color(0xFF6D5378)),
        ColorFamily("gy", L("خاکستری", "Grey", "رمادي", "Серый"), Color(0xFF8D9095)),
        ColorFamily("bk", L("مشکی", "Black", "أسود", "Чёрный"), Color(0xFF1F1F1F)),
    )
    private val colorByCode = colors.associateBy { it.code }
    fun color(code: String): ColorFamily = colorByCode[code] ?: colors.first()

    val patterns: Map<String, L> = linkedMapOf(
        "vein" to L("رگه‌دار", "Veined", "معرّق", "С прожилками"),
        "cloud" to L("ابری", "Clouded", "غائم", "Облачный"),
        "uni" to L("یکنواخت", "Uniform", "متجانس", "Однородный"),
        "grain" to L("دانه‌ای / خال‌دار", "Grained / speckled", "حبيبي / منقّط", "Зернистый / крапчатый"),
        "pore" to L("حفره‌دار", "Porous", "مسامي", "Пористый"),
        "band" to L("نواری / لایه‌ای", "Banded / layered", "مخطط / طبقي", "Полосчатый / слоистый"),
    )

    val finishes: Map<String, L> = linkedMapOf(
        "pol" to L("صیقلی (پولیش)", "Polished", "مصقول", "Полированный"),
        "hon" to L("مات (هونِد)", "Honed", "مطفي (هوند)", "Лощёный (хонингованный)"),
        "fil" to L("فیلرشده", "Filled", "معبأ المسام", "С заполненными порами"),
        "tum" to L("آنتیک (تامبل)", "Tumbled", "معتّق (تامبل)", "Галтованный"),
        "lea" to L("چرمی (لِدر)", "Leathered", "جلدي (ليذر)", "Кожаный (leather)"),
        "fla" to L("حرارتی (فلیم)", "Flamed", "محروق (فليم)", "Термообработанный"),
        "bus" to L("چکشی (بوش‌همر)", "Bush-hammered", "مطروق (بوش هامر)", "Бучардированный"),
        "san" to L("سندبلاست", "Sandblasted", "مسفوع بالرمل", "Пескоструйный"),
        "spl" to L("تیشه‌ای / طبیعی", "Split / natural", "مشقوق / طبيعي", "Колотый / природный"),
    )

    val uses: Map<String, L> = linkedMapOf(
        "fl" to L("کف داخلی", "Indoor floors", "أرضيات داخلية", "Полы в помещении"),
        "wl" to L("دیوار داخلی", "Interior walls", "جدران داخلية", "Внутренние стены"),
        "fa" to L("نمای خارجی", "Facades", "واجهات خارجية", "Фасады"),
        "pv" to L("کف‌پوش محوطه", "Outdoor paving", "رصف خارجي", "Мощение"),
        "st" to L("پله", "Stairs", "درج", "Лестницы"),
        "ct" to L("صفحهٔ کابینت", "Countertops", "أسطح المطابخ", "Столешницы"),
        "bl" to L("بک‌لایت (نور از پشت)", "Backlit panels", "إضاءة خلفية", "С подсветкой"),
        "rf" to L("پوشش بام", "Roofing", "تغطية الأسطح", "Кровля"),
        "mo" to L("مجسمه و تزئینات", "Sculpture & decor", "منحوتات وديكور", "Скульптура и декор"),
    )

    val acid: Map<String, L> = mapOf(
        "strong" to L("می‌جوشد (کربناتی)", "Fizzes (carbonate)", "يفور (كربوناتي)", "Вскипает (карбонатный)"),
        "weak" to L("ضعیف، فقط پودر آن", "Weak, only when powdered", "ضعيف، مسحوقه فقط", "Слабо, только порошок"),
        "none" to L("واکنش ندارد", "No reaction", "لا يتفاعل", "Не реагирует"),
    )

    fun codes(csv: String): List<String> = csv.split(',').map { it.trim() }.filter { it.isNotEmpty() }
}
