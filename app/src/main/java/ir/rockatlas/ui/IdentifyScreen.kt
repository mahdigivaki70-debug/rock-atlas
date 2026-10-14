package ir.rockatlas.ui

import android.widget.Toast
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.PickVisualMediaRequest
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.aspectRatio
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.PhotoCamera
import androidx.compose.material.icons.filled.PhotoLibrary
import androidx.compose.material.icons.outlined.ImageSearch
import androidx.compose.material.icons.outlined.Refresh
import androidx.compose.material3.Button
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.FilledTonalButton
import androidx.compose.material3.FilterChip
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel
import ir.rockatlas.identify.Answer
import ir.rockatlas.identify.FieldTests
import ir.rockatlas.identify.IdentifyViewModel
import ir.rockatlas.identify.ImageIO
import ir.rockatlas.identify.LensLauncher

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun IdentifyScreen(vm: MainViewModel, onStone: (String) -> Unit, onSearch: () -> Unit) {
    val idVm: IdentifyViewModel = viewModel()
    val state by idVm.state.collectAsStateWithLifecycle()
    val typeMap by vm.typeMap.collectAsStateWithLifecycle()
    val images by vm.images.collectAsStateWithLifecycle()
    val context = LocalContext.current
    val str = strings

    val takePicture = rememberLauncherForActivityResult(ActivityResultContracts.TakePicture()) { ok ->
        val uri = idVm.pendingCaptureUri
        if (ok && uri != null) idVm.onImage(uri)
    }
    val pickImage = rememberLauncherForActivityResult(ActivityResultContracts.PickVisualMedia()) { uri ->
        if (uri != null) idVm.onImage(uri)
    }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text(str.identifyTitle) },
                actions = {
                    if (state.bitmap != null) IconButton(onClick = idVm::reset) { Icon(Icons.Outlined.Refresh, str.newPhoto) }
                },
            )
        },
    ) { pad ->
        LazyColumn(contentPadding = PaddingValues(top = pad.calculateTopPadding(), bottom = 24.dp)) {
            item {
                Column(Modifier.padding(horizontal = 16.dp)) {
                    val bmp = state.bitmap
                    if (bmp != null) {
                        Image(
                            bmp.asImageBitmap(), str.stonePhoto,
                            contentScale = ContentScale.Crop,
                            modifier = Modifier.fillMaxWidth().aspectRatio(4f / 3f).clip(RoundedCornerShape(16.dp)),
                        )
                    } else {
                        Text(
                            str.identifyIntro,
                            style = MaterialTheme.typography.bodyMedium,
                        )
                    }
                    Spacer(Modifier.height(12.dp))
                    Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                        Button(onClick = {
                            val uri = ImageIO.newCaptureUri(context)
                            idVm.pendingCaptureUri = uri
                            takePicture.launch(uri)
                        }, modifier = Modifier.weight(1f)) {
                            Icon(Icons.Filled.PhotoCamera, null); Spacer(Modifier.width(6.dp)); Text(str.camera)
                        }
                        FilledTonalButton(onClick = {
                            pickImage.launch(PickVisualMediaRequest(ActivityResultContracts.PickVisualMedia.ImageOnly))
                        }, modifier = Modifier.weight(1f)) {
                            Icon(Icons.Filled.PhotoLibrary, null); Spacer(Modifier.width(6.dp)); Text(str.gallery)
                        }
                    }
                    state.imageUri?.let { uri ->
                        OutlinedButton(
                            onClick = {
                                if (!LensLauncher.open(context, uri)) Toast.makeText(context, str.lensMissing, Toast.LENGTH_LONG).show()
                            },
                            modifier = Modifier.fillMaxWidth().padding(top = 8.dp),
                        ) {
                            Icon(Icons.Outlined.ImageSearch, null); Spacer(Modifier.width(6.dp)); Text(str.askLens)
                        }
                        Text(
                            str.lensNote,
                            style = MaterialTheme.typography.bodySmall,
                            color = MaterialTheme.colorScheme.onSurfaceVariant,
                        )
                        androidx.compose.material3.TextButton(onClick = onSearch) { Text(str.goSearch) }
                    }
                    if (state.busy) LinearProgressIndicator(Modifier.fillMaxWidth().padding(top = 8.dp))
                    if (state.badImage) Text(str.badImage, color = MaterialTheme.colorScheme.error, modifier = Modifier.padding(top = 8.dp))
                }
            }
            if (state.bitmap != null) {
                item { SectionTitle(str.testsTitle) }
                item { Tests(state.tests, idVm::setTests) }
                item {
                    SectionTitle(str.matchesTitle)
                    Text(
                        if (state.modelLoaded) str.matchWithModel else str.matchBasic,
                        style = MaterialTheme.typography.bodySmall,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                        modifier = Modifier.padding(horizontal = 16.dp),
                    )
                }
                items(state.results, key = { it.stone.id }) { m ->
                    StoneRow(m.stone, typeMap[m.stone.typeId], images[m.stone.id], vm::requestImage, onClick = { onStone(m.stone.id) }) {
                        Text("${num((m.score * 100).toInt())}%", style = MaterialTheme.typography.labelLarge, color = MaterialTheme.colorScheme.primary)
                    }
                }
            }
        }
    }
}

@Composable
private fun Tests(t: FieldTests, onChange: (FieldTests) -> Unit) {
    val str = strings
    Column(Modifier.padding(horizontal = 16.dp)) {
        Text(str.acidQ, style = MaterialTheme.typography.bodyMedium)
        LazyRow {
            val opts = listOf(null to str.acidNotTested, "strong" to str.acidFizz, "weak" to str.acidWeak, "none" to str.acidNone)
            items(opts) { (code, label) ->
                FilterChip(selected = t.acid == code, onClick = { onChange(t.copy(acid = code)) }, label = { Text(label) }, modifier = Modifier.padding(end = 6.dp))
            }
        }
        YesNo(str.poresQ, t.pores) { onChange(t.copy(pores = it)) }
        YesNo(str.translucentQ, t.translucent) { onChange(t.copy(translucent = it)) }
        YesNo(str.grainsQ, t.sparklyGrains) { onChange(t.copy(sparklyGrains = it)) }
        YesNo(str.veinsQ, t.veins) { onChange(t.copy(veins = it)) }
    }
}

@Composable
private fun YesNo(q: String, value: Answer, onChange: (Answer) -> Unit) {
    Row(Modifier.fillMaxWidth().padding(top = 6.dp), verticalAlignment = Alignment.CenterVertically) {
        Text(q, style = MaterialTheme.typography.bodyMedium, modifier = Modifier.weight(1f))
        FilterChip(selected = value == Answer.YES, onClick = { onChange(if (value == Answer.YES) Answer.UNKNOWN else Answer.YES) }, label = { Text(strings.yes) })
        Spacer(Modifier.width(6.dp))
        FilterChip(selected = value == Answer.NO, onClick = { onChange(if (value == Answer.NO) Answer.UNKNOWN else Answer.NO) }, label = { Text(strings.no) })
    }
}
