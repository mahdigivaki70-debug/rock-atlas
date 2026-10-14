package ir.rockatlas.ui

import androidx.compose.runtime.Composable
import androidx.compose.runtime.ReadOnlyComposable
import androidx.compose.runtime.staticCompositionLocalOf
import ir.rockatlas.data.Lang
import ir.rockatlas.data.Strings
import java.text.DecimalFormat
import java.text.DecimalFormatSymbols
import java.util.Locale

val LocalLang = staticCompositionLocalOf { Lang.FA }

val strings: Strings
    @Composable @ReadOnlyComposable
    get() = Strings.of(LocalLang.current)

private val fmt = DecimalFormat("#,##0.##", DecimalFormatSymbols(Locale.US))

/** Formats a number with the digits of [lang]: Persian, Arabic-Indic or Latin. */
fun formatNumber(n: Number, lang: Lang): String {
    val latin = fmt.format(n)
    val (zero, group, decimal) = when (lang) {
        Lang.FA -> Triple('۰', '٬', '٫')
        Lang.AR -> Triple('٠', '٬', '٫')
        Lang.EN, Lang.RU -> return if (lang == Lang.RU) latin.replace(',', ' ').replace('.', ',') else latin
    }
    return buildString(latin.length) {
        for (c in latin) append(
            when (c) {
                in '0'..'9' -> zero + (c - '0')
                ',' -> group
                '.' -> decimal
                else -> c
            },
        )
    }
}

@Composable
@ReadOnlyComposable
fun num(n: Number): String = formatNumber(n, LocalLang.current)

@Composable
@ReadOnlyComposable
fun range(min: Double, max: Double): String {
    val lang = LocalLang.current
    if (min == max) return formatNumber(min, lang)
    val to = when (lang) {
        Lang.FA -> "تا"
        Lang.AR -> "إلى"
        Lang.EN, Lang.RU -> "–"
    }
    return "${formatNumber(min, lang)} $to ${formatNumber(max, lang)}"
}
