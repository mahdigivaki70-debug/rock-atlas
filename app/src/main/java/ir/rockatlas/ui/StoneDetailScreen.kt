package ir.rockatlas.ui

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.ExperimentalLayoutApi
import androidx.compose.foundation.layout.FlowRow
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.aspectRatio
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.Favorite
import androidx.compose.material.icons.filled.FavoriteBorder
import androidx.compose.material.icons.outlined.Place
import androidx.compose.material3.AssistChip
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.SuggestionChip
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import ir.rockatlas.data.Labels
import ir.rockatlas.data.StoneType

@OptIn(ExperimentalMaterial3Api::class, ExperimentalLayoutApi::class)
@Composable
fun StoneDetailScreen(vm: MainViewModel, stoneId: String, onBack: () -> Unit, onCategory: (String) -> Unit, onCountry: (String) -> Unit) {
    val stone by remember(stoneId) { vm.repo.stone(stoneId) }.collectAsStateWithLifecycle(null)
    val typeMap by vm.typeMap.collectAsStateWithLifecycle()
    val images by vm.images.collectAsStateWithLifecycle()
    val favorites by vm.favorites.collectAsStateWithLifecycle()
    val context = LocalContext.current
    val lang = LocalLang.current
    val str = strings
    val s = stone
    val isFav = stoneId in favorites

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text(s?.name(lang).orEmpty()) },
                navigationIcon = { IconButton(onClick = onBack) { Icon(Icons.AutoMirrored.Filled.ArrowBack, str.back) } },
                actions = {
                    IconButton(onClick = { vm.toggleFavorite(stoneId) }) {
                        Icon(if (isFav) Icons.Filled.Favorite else Icons.Filled.FavoriteBorder, if (isFav) str.removeFavorite else str.addFavorite)
                    }
                },
            )
        },
    ) { pad ->
        if (s == null) return@Scaffold
        val type = typeMap[s.typeId]
        val image = images[s.id]
        Column(Modifier.padding(top = pad.calculateTopPadding()).verticalScroll(rememberScrollState()).padding(bottom = 24.dp)) {
            StoneImage(s, image, vm::requestImage, Modifier.fillMaxWidth().aspectRatio(4f / 3f))
            if (image != null && image.imageUrl.isNotEmpty()) {
                TextButton(onClick = { openHttps(context, image.filePageUrl) }, modifier = Modifier.padding(horizontal = 8.dp)) {
                    Text(
                        (if (image.generic) str.sampleImage(type?.name(lang).orEmpty()) else "") + str.imageSource,
                        style = MaterialTheme.typography.labelSmall,
                    )
                }
            }
            Column(Modifier.padding(horizontal = 16.dp)) {
                Spacer(Modifier.height(8.dp))
                Text(s.name(lang), style = MaterialTheme.typography.headlineSmall, fontWeight = FontWeight.Bold)
                Text(s.subtitle(lang), style = MaterialTheme.typography.titleSmall, color = MaterialTheme.colorScheme.onSurfaceVariant)
                if (s.aliases.isNotBlank()) {
                    Text("${str.otherNames}: ${s.aliases}", style = MaterialTheme.typography.bodySmall, color = MaterialTheme.colorScheme.onSurfaceVariant)
                }
                Spacer(Modifier.height(10.dp))
                FlowRow {
                    if (type != null) AssistChip(onClick = { onCategory(type.categoryId) }, label = { Text(type.name(lang)) }, modifier = Modifier.padding(end = 6.dp))
                    SuggestionChip(onClick = {}, label = { Text(Labels.color(s.color).name(lang)) }, icon = { ColorDot(s.color) }, modifier = Modifier.padding(end = 6.dp))
                    SuggestionChip(onClick = {}, label = { Text(Labels.patterns[s.pattern]?.get(lang).orEmpty()) })
                }
                Spacer(Modifier.height(8.dp))
                Text(s.desc(lang), style = MaterialTheme.typography.bodyLarge)
            }

            SectionTitle(str.regionTitle)
            Card(
                onClick = { onCountry(s.country) },
                modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp),
                colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surfaceContainer),
            ) {
                Row(Modifier.padding(16.dp), verticalAlignment = Alignment.CenterVertically) {
                    Icon(Icons.Outlined.Place, null, tint = MaterialTheme.colorScheme.primary)
                    Spacer(Modifier.width(10.dp))
                    Column {
                        Text(s.region(lang), style = MaterialTheme.typography.titleMedium)
                        Text(str.countryLine(s.country(lang)), style = MaterialTheme.typography.bodySmall)
                    }
                }
            }

            if (type != null) LabProperties(type)

            SectionTitle(str.usesTitle)
            FlowRow(Modifier.padding(horizontal = 16.dp)) {
                Labels.codes(s.uses).forEach { u -> SuggestionChip(onClick = {}, label = { Text(Labels.uses[u]?.get(lang) ?: u) }, modifier = Modifier.padding(end = 6.dp)) }
            }
            SectionTitle(str.finishesTitle)
            FlowRow(Modifier.padding(horizontal = 16.dp)) {
                Labels.codes(s.finishes).forEach { f -> SuggestionChip(onClick = {}, label = { Text(Labels.finishes[f]?.get(lang) ?: f) }, modifier = Modifier.padding(end = 6.dp)) }
            }
            if (type?.acid == "strong" && "fa" in Labels.codes(s.uses)) {
                Text(
                    str.carbonateTip,
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                    modifier = Modifier.padding(horizontal = 16.dp, vertical = 10.dp),
                )
            }
            s.wikiTitle?.let { title ->
                TextButton(onClick = { openHttps(context, "https://en.wikipedia.org/wiki/" + android.net.Uri.encode(title.replace(' ', '_'))) }, modifier = Modifier.padding(horizontal = 8.dp)) {
                    Text(str.readMore)
                }
            }
        }
    }
}

@Composable
private fun LabProperties(type: StoneType) {
    val lang = LocalLang.current
    val s = strings
    SectionTitle(s.labTitle(type.name(lang)))
    Card(
        modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp),
        colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surfaceContainer),
    ) {
        Column(Modifier.padding(vertical = 4.dp)) {
            PropRow(s.density, "${range(type.densityMin, type.densityMax)} kg/m³")
            PropRow(s.absorption, "${range(type.absorptionMin, type.absorptionMax)} %")
            PropRow(s.compressive, "${range(type.compressiveMin, type.compressiveMax)} MPa")
            PropRow(s.flexural, "${range(type.flexuralMin, type.flexuralMax)} MPa")
            PropRow(s.mohs, range(type.mohsMin, type.mohsMax))
            PropRow(s.acid, Labels.acid[type.acid]?.get(lang).orEmpty())
            PropRow(s.standard, type.standard, last = true)
        }
    }
    Text(
        s.labDisclaimer,
        style = MaterialTheme.typography.bodySmall,
        color = MaterialTheme.colorScheme.onSurfaceVariant,
        modifier = Modifier.padding(horizontal = 16.dp, vertical = 6.dp),
    )
}

@Composable
private fun PropRow(label: String, value: String, last: Boolean = false) {
    Row(Modifier.fillMaxWidth().padding(horizontal = 16.dp, vertical = 10.dp)) {
        Text(label, style = MaterialTheme.typography.bodyMedium, color = MaterialTheme.colorScheme.onSurfaceVariant, modifier = Modifier.weight(1f))
        Text(value, style = MaterialTheme.typography.bodyMedium, fontWeight = FontWeight.Medium)
    }
    if (!last) HorizontalDivider(Modifier.padding(horizontal = 16.dp), color = MaterialTheme.colorScheme.outline.copy(alpha = 0.15f))
}
