package ir.rockatlas.ui

import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.CompositionLocalProvider
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalLayoutDirection
import androidx.compose.ui.unit.LayoutDirection
import ir.rockatlas.data.Lang

private val Light = lightColorScheme(
    primary = Color(0xFF6B4F3A),
    onPrimary = Color.White,
    primaryContainer = Color(0xFFF1DEC9),
    onPrimaryContainer = Color(0xFF2A1B0F),
    secondary = Color(0xFF5E6B5A),
    secondaryContainer = Color(0xFFE0E8D9),
    tertiary = Color(0xFF4F6577),
    background = Color(0xFFF8F4EE),
    surface = Color(0xFFF8F4EE),
    surfaceVariant = Color(0xFFECE3D8),
    surfaceContainer = Color(0xFFF1EBE3),
)

private val Dark = darkColorScheme(
    primary = Color(0xFFDDC0A5),
    onPrimary = Color(0xFF3E2D1F),
    primaryContainer = Color(0xFF574131),
    onPrimaryContainer = Color(0xFFF7E3CF),
    secondary = Color(0xFFC3CEBC),
    secondaryContainer = Color(0xFF444F41),
    tertiary = Color(0xFFB4C9DB),
    background = Color(0xFF1B1714),
    surface = Color(0xFF1B1714),
    surfaceVariant = Color(0xFF3B332C),
    surfaceContainer = Color(0xFF26211D),
)

/** Layout follows the chosen app language: right-to-left for Persian and Arabic. */
@Composable
fun RockAtlasTheme(lang: Lang, content: @Composable () -> Unit) {
    MaterialTheme(colorScheme = if (isSystemInDarkTheme()) Dark else Light) {
        CompositionLocalProvider(
            LocalLang provides lang,
            LocalLayoutDirection provides if (lang.rtl) LayoutDirection.Rtl else LayoutDirection.Ltr,
            content = content,
        )
    }
}
