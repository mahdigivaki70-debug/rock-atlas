package ir.rockatlas.data

/** Folds Persian/Arabic spelling variants so "سنگ‌ها" and "سنگ ها" match. */
object TextNormalizer {
    private const val MAX_QUERY = 60

    fun normalize(input: String): String {
        val sb = StringBuilder(input.length)
        for (ch in input) {
            val c = when (ch) {
                'ي', 'ى', 'ئ' -> 'ی'
                'ك' -> 'ک'
                'ة' -> 'ه'
                'أ', 'إ', 'آ', 'ٱ' -> 'ا'
                'ؤ' -> 'و'
                '‌', '‍', '-', '_', '،', ',', '.', '(', ')' -> ' '
                in '۰'..'۹' -> '0' + (ch - '۰')
                in '٠'..'٩' -> '0' + (ch - '٠')
                else -> ch
            }
            // Drop Arabic diacritics and tatweel.
            if (c in 'ً'..'ٟ' || c == 'ٰ' || c == 'ـ') continue
            sb.append(c.lowercaseChar())
        }
        return sb.toString().replace(Regex("\\s+"), " ").trim()
    }

    /** Sanitises raw user input before it is used as a query. */
    fun cleanQuery(raw: String): String =
        raw.filter { !it.isISOControl() }.take(MAX_QUERY)
}
