package ir.rockatlas.ui

import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.FilterChip
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import ir.rockatlas.data.Labels

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun TypeScreen(vm: MainViewModel, typeId: String, onStone: (String) -> Unit, onBack: () -> Unit) {
    val typeMap by vm.typeMap.collectAsStateWithLifecycle()
    val stones by vm.stones.collectAsStateWithLifecycle()
    val images by vm.images.collectAsStateWithLifecycle()
    val type = typeMap[typeId]
    val inType = stones.filter { it.typeId == typeId }
    val colorsPresent = Labels.colors.filter { c -> inType.any { it.color == c.code } }
    var selected by rememberSaveable { mutableStateOf<String?>(null) }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text(type?.nameFa ?: "") },
                navigationIcon = { IconButton(onClick = onBack) { Icon(Icons.AutoMirrored.Filled.ArrowBack, "بازگشت") } },
            )
        },
    ) { pad ->
        LazyColumn(contentPadding = PaddingValues(top = pad.calculateTopPadding(), bottom = 16.dp)) {
            if (type != null) {
                item { TypeSummary(type) }
            }
            item {
                LazyRow(contentPadding = PaddingValues(horizontal = 16.dp)) {
                    item {
                        FilterChip(selected = selected == null, onClick = { selected = null }, label = { Text("همه") }, modifier = Modifier.padding(end = 6.dp))
                    }
                    items(colorsPresent) { c ->
                        FilterChip(
                            selected = selected == c.code,
                            onClick = { selected = if (selected == c.code) null else c.code },
                            label = { Text(c.fa) },
                            leadingIcon = { ColorDot(c.code) },
                            modifier = Modifier.padding(end = 6.dp),
                        )
                    }
                }
            }
            // Subcategories: one section per colour family.
            for (c in colorsPresent) {
                if (selected != null && selected != c.code) continue
                val group = inType.filter { it.color == c.code }
                item(key = "h_${c.code}") {
                    Row { SectionTitle("${type?.nameFa ?: ""} ${c.fa} (${fa(group.size)})") }
                }
                items(group, key = { it.id }) { s ->
                    StoneRow(s, type, images[s.id], vm::requestImage, onClick = { onStone(s.id) })
                }
            }
        }
    }
}

@Composable
private fun TypeSummary(type: ir.rockatlas.data.StoneType) {
    androidx.compose.foundation.layout.Column(Modifier.padding(horizontal = 16.dp, vertical = 8.dp)) {
        Text(type.description, style = MaterialTheme.typography.bodyMedium)
        Text(
            "چگالی ${faRange(type.densityMin, type.densityMax)} kg/m³ · جذب آب ${faRange(type.absorptionMin, type.absorptionMax)}٪ · مقاومت فشاری ${faRange(type.compressiveMin, type.compressiveMax)} MPa",
            style = MaterialTheme.typography.bodySmall,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
            modifier = Modifier.padding(top = 6.dp),
        )
    }
}
