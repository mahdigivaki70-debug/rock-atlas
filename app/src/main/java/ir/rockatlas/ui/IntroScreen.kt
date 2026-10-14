package ir.rockatlas.ui

import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.ExperimentalLayoutApi
import androidx.compose.foundation.layout.FlowRow
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.material3.FilterChip
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import ir.rockatlas.R
import kotlinx.coroutines.delay

/** Opening screen with the app name and creator details; tap or wait to continue. */
@OptIn(ExperimentalLayoutApi::class)
@Composable
fun IntroScreen(onDone: () -> Unit, onLang: (ir.rockatlas.data.Lang) -> Unit) {
    val str = strings
    val current = LocalLang.current
    LaunchedEffect(Unit) {
        delay(3500)
        onDone()
    }
    Box(
        Modifier.fillMaxSize().background(MaterialTheme.colorScheme.primaryContainer).clickable(onClick = onDone),
        contentAlignment = Alignment.Center,
    ) {
        Column(horizontalAlignment = Alignment.CenterHorizontally, verticalArrangement = Arrangement.Center, modifier = Modifier.padding(32.dp)) {
            Image(painterResource(R.drawable.ic_launcher_foreground), null, Modifier.size(140.dp))
            Text(str.appName, style = MaterialTheme.typography.headlineSmall, fontWeight = FontWeight.Bold, textAlign = TextAlign.Center)
            Spacer(Modifier.height(32.dp))
            Text(str.madeBy, style = MaterialTheme.typography.labelLarge, color = MaterialTheme.colorScheme.primary)
            Text(str.author, style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.Bold)
            Spacer(Modifier.height(8.dp))
            Text("⁦${Credits.PHONE}⁩", style = MaterialTheme.typography.titleMedium)
            Text(Credits.WEBSITE, style = MaterialTheme.typography.titleMedium, color = MaterialTheme.colorScheme.primary)
            Spacer(Modifier.height(28.dp))
            // Language choice right on the first screen; tapping one also enters the app.
            FlowRow(horizontalArrangement = Arrangement.spacedBy(6.dp, Alignment.CenterHorizontally)) {
                ir.rockatlas.data.Lang.entries.forEach { l ->
                    FilterChip(selected = l == current, onClick = { onLang(l); onDone() }, label = { Text(l.nativeName) })
                }
            }
            Spacer(Modifier.height(16.dp))
            Text(str.tapToEnter, style = MaterialTheme.typography.bodySmall, color = MaterialTheme.colorScheme.onSurfaceVariant)
        }
    }
}
