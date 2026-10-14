package ir.rockatlas.ui

import android.content.ActivityNotFoundException
import android.content.Context
import android.content.Intent
import android.net.Uri
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.width
import androidx.compose.material.icons.outlined.Language
import androidx.compose.material.icons.outlined.Phone
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.TextButton
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AboutScreen(onBack: () -> Unit) {
    val str = strings
    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text(str.aboutTitle) },
                navigationIcon = { IconButton(onClick = onBack) { Icon(Icons.AutoMirrored.Filled.ArrowBack, str.back) } },
            )
        },
    ) { pad ->
        Column(Modifier.padding(top = pad.calculateTopPadding()).verticalScroll(rememberScrollState()).padding(16.dp)) {
            CreditsCard()
            Spacer(Modifier.height(8.dp))
            Para(str.aboutIntro)
            Head(str.aboutLabHead)
            Para(str.aboutLabText)
            Head(str.aboutImagesHead)
            Para(str.aboutImagesText)
            Head(str.aboutIdentHead)
            Para(str.aboutIdentText)
            Head(str.aboutPrivacyHead)
            Para(str.aboutPrivacyText)
        }
    }
}

@Composable
fun CreditsCard() {
    val context = LocalContext.current
    Card(
        modifier = Modifier.fillMaxWidth(),
        colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.primaryContainer),
    ) {
        Column(Modifier.padding(16.dp)) {
            Text(strings.creator, style = MaterialTheme.typography.labelLarge, color = MaterialTheme.colorScheme.primary)
            Text(strings.author, style = MaterialTheme.typography.titleLarge, fontWeight = FontWeight.Bold)
            Spacer(Modifier.height(8.dp))
            TextButton(onClick = { dial(context, Credits.PHONE) }) {
                Icon(Icons.Outlined.Phone, null)
                Spacer(Modifier.width(8.dp))
                // Phone numbers read left-to-right even inside Persian text.
                Text("\u2066${Credits.PHONE}\u2069")
            }
            TextButton(onClick = { openHttps(context, Credits.WEBSITE_URL) }) {
                Icon(Icons.Outlined.Language, null)
                Spacer(Modifier.width(8.dp))
                Text(Credits.WEBSITE)
            }
        }
    }
}

object Credits {
    const val PHONE = "+989192950266"
    const val WEBSITE = "www.nexstone.ir"
    const val WEBSITE_URL = "https://www.nexstone.ir"
}

/** Opens the dialer with the number filled in; needs no CALL_PHONE permission. */
private fun dial(context: Context, phone: String) {
    try {
        context.startActivity(Intent(Intent.ACTION_DIAL, Uri.fromParts("tel", phone, null)))
    } catch (e: ActivityNotFoundException) {
    }
}

@Composable
private fun Head(t: String) = Text(t, style = MaterialTheme.typography.titleMedium, color = MaterialTheme.colorScheme.primary, modifier = Modifier.padding(top = 16.dp, bottom = 4.dp))

@Composable
private fun Para(t: String) = Text(t, style = MaterialTheme.typography.bodyMedium)
