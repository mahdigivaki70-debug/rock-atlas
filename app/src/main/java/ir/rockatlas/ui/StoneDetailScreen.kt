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
fun StoneDetailScreen(vm: MainViewModel, stoneId: String, onBack: () -> Unit, onType: (String) -> Unit, onCountry: (String) -> Unit) {
    val stone by remember(stoneId) { vm.repo.stone(stoneId) }.collectAsStateWithLifecycle(null)
    val typeMap by vm.typeMap.collectAsStateWithLifecycle()
    val images by vm.images.collectAsStateWithLifecycle()
    val favorites by vm.favorites.collectAsStateWithLifecycle()
    val context = LocalContext.current
    val s = stone
    val isFav = stoneId in favorites

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text(s?.nameFa ?: "") },
                navigationIcon = { IconButton(onClick = onBack) { Icon(Icons.AutoMirrored.Filled.ArrowBack, "بازگشت") } },
                actions = {
                    IconButton(onClick = { vm.toggleFavorite(stoneId) }) {
                        Icon(if (isFav) Icons.Filled.Favorite else Icons.Filled.FavoriteBorder, if (isFav) "حذف از علاقه‌مندی‌ها" else "افزودن به علاقه‌مندی‌ها")
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
                        (if (image.generic) "تصویر نمونه از ${type?.nameFa ?: "این نوع سنگ"}، نه همین سنگ. " else "") +
                            "منبع: ویکی‌مدیا کامانز (پدیدآورنده و مجوز در صفحهٔ فایل)",
                        style = MaterialTheme.typography.labelSmall,
                    )
                }
            }
            Column(Modifier.padding(horizontal = 16.dp)) {
                Spacer(Modifier.height(8.dp))
                Text(s.nameFa, style = MaterialTheme.typography.headlineSmall, fontWeight = FontWeight.Bold)
                Text(s.nameEn, style = MaterialTheme.typography.titleSmall, color = MaterialTheme.colorScheme.onSurfaceVariant)
                if (s.aliases.isNotBlank()) {
                    Text("نام‌های دیگر: ${s.aliases}", style = MaterialTheme.typography.bodySmall, color = MaterialTheme.colorScheme.onSurfaceVariant)
                }
                Spacer(Modifier.height(10.dp))
                FlowRow {
                    if (type != null) AssistChip(onClick = { onType(type.id) }, label = { Text(type.nameFa) }, modifier = Modifier.padding(end = 6.dp))
                    SuggestionChip(onClick = {}, label = { Text(Labels.color(s.color).fa) }, icon = { ColorDot(s.color) }, modifier = Modifier.padding(end = 6.dp))
                    SuggestionChip(onClick = {}, label = { Text(Labels.patterns[s.pattern].orEmpty()) })
                }
                Spacer(Modifier.height(8.dp))
                Text(s.description, style = MaterialTheme.typography.bodyLarge)
            }

            SectionTitle("منطقه و معدن")
            Card(
                onClick = { onCountry(s.country) },
                modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp),
                colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surfaceContainer),
            ) {
                Row(Modifier.padding(16.dp), verticalAlignment = Alignment.CenterVertically) {
                    Icon(Icons.Outlined.Place, null, tint = MaterialTheme.colorScheme.primary)
                    Spacer(Modifier.width(10.dp))
                    Column {
                        Text(s.region, style = MaterialTheme.typography.titleMedium)
                        Text("کشور: ${s.country} · دیدن سنگ‌های دیگر این کشور", style = MaterialTheme.typography.bodySmall)
                    }
                }
            }

            if (type != null) LabProperties(type)

            SectionTitle("کاربردهای پیشنهادی")
            FlowRow(Modifier.padding(horizontal = 16.dp)) {
                Labels.codes(s.uses).forEach { u -> SuggestionChip(onClick = {}, label = { Text(Labels.uses[u] ?: u) }, modifier = Modifier.padding(end = 6.dp)) }
            }
            SectionTitle("فرآوری‌های رایج سطح")
            FlowRow(Modifier.padding(horizontal = 16.dp)) {
                Labels.codes(s.finishes).forEach { f -> SuggestionChip(onClick = {}, label = { Text(Labels.finishes[f] ?: f) }, modifier = Modifier.padding(end = 6.dp)) }
            }
            if (type?.acid == "strong" && "fa" in Labels.codes(s.uses)) {
                Text(
                    "نکته: سنگ‌های کربناتی در برابر باران اسیدی و شوینده‌های اسیدی حساس‌اند؛ برای نما، سنگ را آب‌گریز (ضدآب) کنید و با شوینده‌های خنثی تمیز کنید.",
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                    modifier = Modifier.padding(horizontal = 16.dp, vertical = 10.dp),
                )
            }
            s.wikiTitle?.let { title ->
                TextButton(onClick = { openHttps(context, "https://en.wikipedia.org/wiki/" + android.net.Uri.encode(title.replace(' ', '_'))) }, modifier = Modifier.padding(horizontal = 8.dp)) {
                    Text("مطالعهٔ بیشتر در ویکی‌پدیا")
                }
            }
        }
    }
}

@Composable
private fun LabProperties(type: StoneType) {
    SectionTitle("مشخصات آزمایشگاهی (${type.nameFa})")
    Card(
        modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp),
        colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surfaceContainer),
    ) {
        Column(Modifier.padding(vertical = 4.dp)) {
            PropRow("چگالی (وزن مخصوص)", "${faRange(type.densityMin, type.densityMax)} kg/m³")
            PropRow("جذب آب", "${faRange(type.absorptionMin, type.absorptionMax)} ٪")
            PropRow("مقاومت فشاری", "${faRange(type.compressiveMin, type.compressiveMax)} MPa")
            PropRow("مقاومت خمشی", "${faRange(type.flexuralMin, type.flexuralMax)} MPa")
            PropRow("سختی موس", faRange(type.mohsMin, type.mohsMax))
            PropRow("واکنش با اسید", Labels.acid[type.acid].orEmpty())
            PropRow("استاندارد مرجع", type.standard, last = true)
        }
    }
    Text(
        "این اعداد محدودهٔ معمول برای این نوع سنگ است، نه نتیجهٔ آزمایش همین معدن. برای پروژه، برگهٔ آزمایش (گزارش آزمون) سنگ را از فروشنده بخواهید.",
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
