package ir.rockatlas.ui

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
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
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import ir.rockatlas.data.Labels
import ir.rockatlas.data.StoneType

/**
 * One category (e.g. marble). Subcategories are the stone types inside it
 * (e.g. marble > chini, marmarite, serpentinite); colour chips narrow the list.
 */
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun CategoryScreen(vm: MainViewModel, categoryId: String, onStone: (String) -> Unit, onBack: () -> Unit) {
    val categories by vm.categories.collectAsStateWithLifecycle()
    val typeMap by vm.typeMap.collectAsStateWithLifecycle()
    val stones by vm.stones.collectAsStateWithLifecycle()
    val images by vm.images.collectAsStateWithLifecycle()
    val lang = LocalLang.current
    val s = strings
    val category = categories.firstOrNull { it.id == categoryId }
    val subTypes = typeMap.values.filter { it.categoryId == categoryId }.sortedBy { it.sortOrder }
    val inCategory = stones.filter { typeMap[it.typeId]?.categoryId == categoryId }
    val colorsPresent = Labels.colors.filter { c -> inCategory.any { it.color == c.code } }
    var selectedType by rememberSaveable { mutableStateOf<String?>(null) }
    var selectedColor by rememberSaveable { mutableStateOf<String?>(null) }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text(category?.name(lang).orEmpty()) },
                navigationIcon = { IconButton(onClick = onBack) { Icon(Icons.AutoMirrored.Filled.ArrowBack, s.back) } },
            )
        },
    ) { pad ->
        LazyColumn(contentPadding = PaddingValues(top = pad.calculateTopPadding(), bottom = 16.dp)) {
            if (subTypes.size > 1) {
                item {
                    LazyRow(contentPadding = PaddingValues(horizontal = 16.dp, vertical = 2.dp)) {
                        item {
                            FilterChip(selected = selectedType == null, onClick = { selectedType = null }, label = { Text(s.all) }, modifier = Modifier.padding(end = 6.dp))
                        }
                        items(subTypes, key = { it.id }) { t ->
                            FilterChip(
                                selected = selectedType == t.id,
                                onClick = { selectedType = if (selectedType == t.id) null else t.id },
                                label = { Text(t.name(lang)) },
                                modifier = Modifier.padding(end = 6.dp),
                            )
                        }
                    }
                }
            }
            item {
                LazyRow(contentPadding = PaddingValues(horizontal = 16.dp, vertical = 2.dp)) {
                    item {
                        FilterChip(selected = selectedColor == null, onClick = { selectedColor = null }, label = { Text(s.all) }, modifier = Modifier.padding(end = 6.dp))
                    }
                    items(colorsPresent, key = { it.code }) { c ->
                        FilterChip(
                            selected = selectedColor == c.code,
                            onClick = { selectedColor = if (selectedColor == c.code) null else c.code },
                            label = { Text(c.name(lang)) },
                            leadingIcon = { ColorDot(c.code) },
                            modifier = Modifier.padding(end = 6.dp),
                        )
                    }
                }
            }
            for (type in subTypes) {
                if (selectedType != null && selectedType != type.id) continue
                val group = inCategory.filter { it.typeId == type.id && (selectedColor == null || it.color == selectedColor) }
                if (group.isEmpty()) continue
                item(key = "h_${type.id}") { TypeHeader(type, group.size) }
                items(group, key = { it.id }) { st ->
                    StoneRow(st, type, images[st.id], vm::requestImage, onClick = { onStone(st.id) })
                }
            }
        }
    }
}

@Composable
private fun TypeHeader(type: StoneType, count: Int) {
    val lang = LocalLang.current
    val s = strings
    Column(Modifier.padding(start = 16.dp, end = 16.dp, top = 16.dp, bottom = 6.dp)) {
        Text("${type.name(lang)} (${num(count)})", style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.SemiBold, color = MaterialTheme.colorScheme.primary)
        Text(type.desc(lang), style = MaterialTheme.typography.bodySmall)
        Text(
            "${s.density} ${range(type.densityMin, type.densityMax)} kg/m³ · ${s.absorption} ${range(type.absorptionMin, type.absorptionMax)}% · ${s.compressive} ${range(type.compressiveMin, type.compressiveMax)} MPa",
            style = MaterialTheme.typography.labelSmall,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
            modifier = Modifier.padding(top = 4.dp),
        )
    }
}
