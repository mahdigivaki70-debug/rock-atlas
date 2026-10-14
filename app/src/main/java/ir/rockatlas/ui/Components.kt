package ir.rockatlas.ui

import android.content.ActivityNotFoundException
import android.content.Context
import android.content.Intent
import android.net.Uri
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.outlined.Landscape
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import coil.compose.SubcomposeAsyncImage
import ir.rockatlas.data.CachedImage
import ir.rockatlas.data.Labels
import ir.rockatlas.data.Stone
import ir.rockatlas.data.StoneType
import androidx.compose.material3.Icon

@Composable
fun StoneImage(
    stone: Stone,
    image: CachedImage?,
    onNeedImage: (String) -> Unit,
    modifier: Modifier = Modifier,
) {
    LaunchedEffect(stone.id, image) { if (image == null) onNeedImage(stone.id) }
    val swatch = Labels.color(stone.color).swatch
    Box(modifier.background(swatch.copy(alpha = 0.55f)), contentAlignment = Alignment.Center) {
        val url = image?.imageUrl
        if (!url.isNullOrEmpty()) {
            SubcomposeAsyncImage(
                model = url,
                contentDescription = stone.name(LocalLang.current),
                contentScale = ContentScale.Crop,
                modifier = Modifier.fillMaxSize(),
                loading = { PlaceholderIcon() },
                error = { PlaceholderIcon() },
            )
        } else {
            PlaceholderIcon()
        }
    }
}

@Composable
private fun PlaceholderIcon() {
    Box(Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
        Icon(Icons.Outlined.Landscape, null, tint = Color.White.copy(alpha = 0.8f), modifier = Modifier.size(36.dp))
    }
}

@Composable
fun ColorDot(code: String, size: Int = 14) {
    Box(
        Modifier.size(size.dp).clip(CircleShape).background(Labels.color(code).swatch)
            .border(1.dp, MaterialTheme.colorScheme.outline.copy(alpha = 0.4f), CircleShape),
    )
}

@Composable
fun StoneRow(
    stone: Stone,
    type: StoneType?,
    image: CachedImage?,
    onNeedImage: (String) -> Unit,
    onClick: () -> Unit,
    trailing: (@Composable () -> Unit)? = null,
) {
    Card(
        onClick = onClick,
        modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp, vertical = 5.dp),
        colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surfaceContainer),
    ) {
        Row(verticalAlignment = Alignment.CenterVertically) {
            StoneImage(stone, image, onNeedImage, Modifier.size(84.dp).clip(RoundedCornerShape(12.dp)))
            Column(Modifier.weight(1f).padding(horizontal = 12.dp, vertical = 8.dp)) {
                val lang = LocalLang.current
                Text(stone.name(lang), style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.SemiBold, maxLines = 1, overflow = TextOverflow.Ellipsis)
                Text(stone.subtitle(lang), style = MaterialTheme.typography.bodySmall, color = MaterialTheme.colorScheme.onSurfaceVariant, maxLines = 1)
                Spacer(Modifier.height(4.dp))
                Row(verticalAlignment = Alignment.CenterVertically, horizontalArrangement = Arrangement.spacedBy(6.dp)) {
                    ColorDot(stone.color)
                    Text(
                        listOfNotNull(type?.name(lang), stone.place(lang)).joinToString(" · "),
                        style = MaterialTheme.typography.bodySmall,
                        maxLines = 1,
                        overflow = TextOverflow.Ellipsis,
                    )
                }
            }
            if (trailing != null) {
                trailing()
                Spacer(Modifier.width(12.dp))
            }
        }
    }
}

@Composable
fun SectionTitle(text: String, modifier: Modifier = Modifier) {
    Text(
        text,
        style = MaterialTheme.typography.titleSmall,
        color = MaterialTheme.colorScheme.primary,
        modifier = modifier.padding(start = 16.dp, end = 16.dp, top = 16.dp, bottom = 6.dp),
    )
}

@Composable
fun EmptyNote(text: String) {
    Text(text, style = MaterialTheme.typography.bodyMedium, color = MaterialTheme.colorScheme.onSurfaceVariant, modifier = Modifier.padding(24.dp))
}

/** Opens only https links, in the user's browser. */
fun openHttps(context: Context, url: String) {
    val uri = Uri.parse(url)
    if (uri.scheme != "https") return
    try {
        context.startActivity(Intent(Intent.ACTION_VIEW, uri).addCategory(Intent.CATEGORY_BROWSABLE))
    } catch (e: ActivityNotFoundException) {
    }
}

fun Modifier.clickableIf(enabled: Boolean, onClick: () -> Unit) = if (enabled) clickable(onClick = onClick) else this
