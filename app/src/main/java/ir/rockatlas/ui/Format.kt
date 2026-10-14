package ir.rockatlas.ui

import java.text.DecimalFormat
import java.text.DecimalFormatSymbols
import java.util.Locale

private val fmt = DecimalFormat("#,##0.##", DecimalFormatSymbols(Locale.US))

/** Formats a number with Persian digits. */
fun fa(n: Number): String = toFaDigits(fmt.format(n))

fun faRange(min: Double, max: Double): String = if (min == max) fa(min) else "${fa(min)} تا ${fa(max)}"

fun toFaDigits(s: String): String = buildString(s.length) {
    for (c in s) append(
        when (c) {
            in '0'..'9' -> '۰' + (c - '0')
            ',' -> '٬'
            '.' -> '٫'
            else -> c
        },
    )
}
