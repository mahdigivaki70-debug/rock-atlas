package ir.rockatlas.ui

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Check
import androidx.compose.material.icons.filled.Favorite
import androidx.compose.material.icons.outlined.Info
import androidx.compose.material.icons.outlined.Translate
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.DropdownMenu
import androidx.compose.material3.DropdownMenuItem
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import ir.rockatlas.data.Lang

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AtlasScreen(vm: MainViewModel, onCategory: (String) -> Unit, onFavorites: () -> Unit, onAbout: () -> Unit) {
    val categories by vm.categories.collectAsStateWithLifecycle()
    val types by vm.typeMap.collectAsStateWithLifecycle()
    val stones by vm.stones.collectAsStateWithLifecycle()
    val favorites by vm.favorites.collectAsStateWithLifecycle()
    val lang = LocalLang.current
    val s = strings
    val byCategory = stones.groupBy { types[it.typeId]?.categoryId }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text(s.appName) },
                actions = {
                    LanguageMenu(lang, vm::setLang)
                    IconButton(onClick = onAbout) { Icon(Icons.Outlined.Info, s.about) }
                },
            )
        },
    ) { pad ->
        LazyColumn(contentPadding = PaddingValues(top = pad.calculateTopPadding(), bottom = 16.dp)) {
            item {
                Text(
                    s.atlasSummary(num(stones.size), num(categories.size)),
                    style = MaterialTheme.typography.bodyMedium,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                    modifier = Modifier.padding(horizontal = 16.dp, vertical = 8.dp),
                )
            }
            if (favorites.isNotEmpty()) {
                item {
                    Card(
                        onClick = onFavorites,
                        modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp, vertical = 6.dp),
                        colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.primaryContainer),
                    ) {
                        Row(Modifier.padding(16.dp), verticalAlignment = Alignment.CenterVertically) {
                            Icon(Icons.Filled.Favorite, null)
                            Text("  " + s.favorites(num(favorites.size)), style = MaterialTheme.typography.titleMedium)
                        }
                    }
                }
            }
            items(categories, key = { it.id }) { cat ->
                val list = byCategory[cat.id].orEmpty()
                val subTypes = types.values.filter { it.categoryId == cat.id }.sortedBy { it.sortOrder }
                Card(
                    onClick = { onCategory(cat.id) },
                    modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp, vertical = 6.dp),
                    colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surfaceContainer),
                ) {
                    Column(Modifier.padding(16.dp)) {
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            Text(cat.name(lang), style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.Bold, modifier = Modifier.weight(1f))
                            Text(s.stones(num(list.size)), style = MaterialTheme.typography.labelLarge, color = MaterialTheme.colorScheme.primary)
                        }
                        if (lang != Lang.EN) {
                            Text(cat.nameEn, style = MaterialTheme.typography.bodySmall, color = MaterialTheme.colorScheme.onSurfaceVariant)
                        }
                        Spacer(Modifier.height(6.dp))
                        Text(
                            if (subTypes.size > 1) subTypes.joinToString(" · ") { it.name(lang) } else subTypes.firstOrNull()?.desc(lang).orEmpty(),
                            style = MaterialTheme.typography.bodyMedium,
                            maxLines = 2,
                            overflow = TextOverflow.Ellipsis,
                        )
                        Spacer(Modifier.height(8.dp))
                        Row(horizontalArrangement = Arrangement.spacedBy(4.dp)) {
                            list.map { it.color }.distinct().forEach { ColorDot(it) }
                        }
                    }
                }
            }
            item {
                Text(
                    s.categoriesNote,
                    style = MaterialTheme.typography.labelSmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                    modifier = Modifier.padding(horizontal = 16.dp, vertical = 4.dp),
                )
            }
            item {
                TextButton(onClick = onAbout, modifier = Modifier.fillMaxWidth().padding(top = 8.dp)) {
                    Text(
                        "${s.madeBy} ${s.author} · ${Credits.WEBSITE}",
                        style = MaterialTheme.typography.bodySmall,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                    )
                }
            }
        }
    }
}

@Composable
fun LanguageMenu(current: Lang, onSelect: (Lang) -> Unit) {
    var open by remember { mutableStateOf(false) }
    Box {
        IconButton(onClick = { open = true }) { Icon(Icons.Outlined.Translate, strings.language) }
        DropdownMenu(expanded = open, onDismissRequest = { open = false }) {
            Lang.entries.forEach { l ->
                DropdownMenuItem(
                    text = { Text(l.nativeName) },
                    onClick = { open = false; onSelect(l) },
                    trailingIcon = { if (l == current) Icon(Icons.Filled.Check, null) },
                )
            }
        }
    }
}
