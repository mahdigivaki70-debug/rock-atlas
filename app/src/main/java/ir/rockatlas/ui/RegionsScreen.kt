package ir.rockatlas.ui

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ExpandLess
import androidx.compose.material.icons.filled.ExpandMore
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.lifecycle.compose.collectAsStateWithLifecycle

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun RegionsScreen(vm: MainViewModel, onStone: (String) -> Unit) {
    val stones by vm.stones.collectAsStateWithLifecycle()
    val typeMap by vm.typeMap.collectAsStateWithLifecycle()
    val images by vm.images.collectAsStateWithLifecycle()
    var open by rememberSaveable { mutableStateOf("ایران") }

    val byCountry = remember(stones) {
        stones.groupBy { it.country }.entries
            .sortedWith(compareByDescending<Map.Entry<String, List<ir.rockatlas.data.Stone>>> { it.key == "ایران" }.thenByDescending { it.value.size })
    }

    Scaffold(topBar = { TopAppBar(title = { Text("مناطق و معادن") }) }) { pad ->
        LazyColumn(contentPadding = PaddingValues(top = pad.calculateTopPadding(), bottom = 16.dp)) {
            item {
                Text(
                    "هر سنگ از کدام کشور و شهر استخراج می‌شود. روی هر کشور بزنید.",
                    style = MaterialTheme.typography.bodyMedium,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                    modifier = Modifier.padding(horizontal = 16.dp, vertical = 8.dp),
                )
            }
            for ((country, list) in byCountry) {
                val expanded = open == country
                item(key = "c_$country") {
                    Row(
                        Modifier.fillMaxWidth().clickable { open = if (expanded) "" else country }.padding(horizontal = 16.dp, vertical = 14.dp),
                        verticalAlignment = Alignment.CenterVertically,
                    ) {
                        Text(country, style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.SemiBold, modifier = Modifier.weight(1f))
                        Text("${fa(list.size)} سنگ  ", style = MaterialTheme.typography.labelLarge, color = MaterialTheme.colorScheme.primary)
                        Icon(if (expanded) Icons.Filled.ExpandLess else Icons.Filled.ExpandMore, null)
                    }
                    HorizontalDivider(color = MaterialTheme.colorScheme.outline.copy(alpha = 0.15f))
                }
                if (expanded) {
                    val byRegion = list.groupBy { it.region }.toSortedMap()
                    for ((region, rs) in byRegion) {
                        item(key = "r_${country}_$region") { SectionTitle(region) }
                        items(rs, key = { "s_${it.id}" }) { s ->
                            StoneRow(s, typeMap[s.typeId], images[s.id], vm::requestImage, onClick = { onStone(s.id) })
                        }
                    }
                }
            }
        }
    }
}
