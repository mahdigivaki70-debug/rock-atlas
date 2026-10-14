package ir.rockatlas.ui

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Clear
import androidx.compose.material.icons.filled.Favorite
import androidx.compose.material.icons.filled.Search
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.FilterChip
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalFocusManager
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.unit.dp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import ir.rockatlas.data.Labels
import ir.rockatlas.data.SearchEngine
import ir.rockatlas.data.SearchFilters
import ir.rockatlas.data.TextNormalizer
import kotlinx.coroutines.delay

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun SearchScreen(vm: MainViewModel, initialCountry: String?, initialFavorites: Boolean, onStone: (String) -> Unit) {
    val stones by vm.stones.collectAsStateWithLifecycle()
    val typeMap by vm.typeMap.collectAsStateWithLifecycle()
    val types by vm.types.collectAsStateWithLifecycle()
    val images by vm.images.collectAsStateWithLifecycle()
    val favorites by vm.favorites.collectAsStateWithLifecycle()
    val focus = LocalFocusManager.current

    var query by rememberSaveable { mutableStateOf("") }
    var debounced by rememberSaveable { mutableStateOf("") }
    var typeId by rememberSaveable { mutableStateOf<String?>(null) }
    var color by rememberSaveable { mutableStateOf<String?>(null) }
    var use by rememberSaveable { mutableStateOf<String?>(null) }
    var country by rememberSaveable { mutableStateOf(initialCountry) }
    var onlyFav by rememberSaveable { mutableStateOf(initialFavorites) }

    LaunchedEffect(query) {
        delay(200)
        debounced = query
    }
    val filters = SearchFilters(typeId, color, use, country, onlyFav)
    val results = remember(debounced, filters, stones, typeMap, favorites) {
        SearchEngine.search(debounced, filters, stones, typeMap, favorites)
    }
    val countries = remember(stones) {
        stones.groupingBy { it.country }.eachCount().entries
            .sortedWith(compareByDescending<Map.Entry<String, Int>> { it.key == "ایران" }.thenByDescending { it.value })
            .map { it.key }
    }
    val anyFilter = typeId != null || color != null || use != null || country != null || onlyFav

    Scaffold(topBar = { TopAppBar(title = { Text("جستجو") }) }) { pad ->
        LazyColumn(contentPadding = PaddingValues(top = pad.calculateTopPadding(), bottom = 16.dp)) {
            item {
                OutlinedTextField(
                    value = query,
                    onValueChange = { query = TextNormalizer.cleanQuery(it) },
                    modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp, vertical = 8.dp),
                    singleLine = true,
                    placeholder = { Text("نام سنگ، معدن، شهر، رنگ…  مثلاً تراورتن محلات") },
                    leadingIcon = { Icon(Icons.Filled.Search, null) },
                    trailingIcon = {
                        if (query.isNotEmpty()) IconButton(onClick = { query = "" }) { Icon(Icons.Filled.Clear, "پاک کردن") }
                    },
                    keyboardOptions = KeyboardOptions(imeAction = ImeAction.Search),
                    keyboardActions = androidx.compose.foundation.text.KeyboardActions(onSearch = { focus.clearFocus() }),
                )
            }
            item {
                Column {
                    ChipRow(
                        "نوع",
                        types.map { it.id to it.nameFa },
                        typeId,
                    ) { typeId = it }
                    ChipRow("رنگ", Labels.colors.map { it.code to it.fa }, color, dot = true) { color = it }
                    ChipRow("کاربرد", Labels.uses.entries.map { it.key to it.value }, use) { use = it }
                    ChipRow("کشور", countries.map { it to it }, country) { country = it }
                    LazyRow(contentPadding = PaddingValues(horizontal = 16.dp)) {
                        item {
                            FilterChip(
                                selected = onlyFav,
                                onClick = { onlyFav = !onlyFav },
                                label = { Text("فقط علاقه‌مندی‌ها") },
                                leadingIcon = { Icon(Icons.Filled.Favorite, null) },
                            )
                        }
                        if (anyFilter) item {
                            TextButton(onClick = { typeId = null; color = null; use = null; country = null; onlyFav = false }) {
                                Text("حذف همهٔ فیلترها")
                            }
                        }
                    }
                }
            }
            item {
                Text(
                    "${fa(results.size)} نتیجه",
                    style = MaterialTheme.typography.labelLarge,
                    color = MaterialTheme.colorScheme.primary,
                    modifier = Modifier.padding(horizontal = 16.dp, vertical = 8.dp),
                )
            }
            if (results.isEmpty()) item { EmptyNote("سنگی با این مشخصات پیدا نشد. املای دیگری را امتحان کنید یا فیلترها را کم کنید.") }
            items(results, key = { it.id }) { s ->
                StoneRow(s, typeMap[s.typeId], images[s.id], vm::requestImage, onClick = { onStone(s.id) })
            }
        }
    }
}

@Composable
private fun ChipRow(
    title: String,
    options: List<Pair<String, String>>,
    selected: String?,
    dot: Boolean = false,
    onSelect: (String?) -> Unit,
) {
    LazyRow(contentPadding = PaddingValues(horizontal = 16.dp, vertical = 2.dp)) {
        item {
            Text(title, style = MaterialTheme.typography.labelMedium, color = MaterialTheme.colorScheme.onSurfaceVariant, modifier = Modifier.padding(top = 14.dp, end = 8.dp))
        }
        items(options, key = { it.first }) { (code, label) ->
            FilterChip(
                selected = selected == code,
                onClick = { onSelect(if (selected == code) null else code) },
                label = { Text(label) },
                leadingIcon = if (dot) ({ ColorDot(code) }) else null,
                modifier = Modifier.padding(end = 6.dp),
            )
        }
    }
}
