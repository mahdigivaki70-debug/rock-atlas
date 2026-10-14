package ir.rockatlas.ui

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import ir.rockatlas.RockAtlasApp
import ir.rockatlas.data.CachedImage
import ir.rockatlas.data.Stone
import ir.rockatlas.data.StoneType
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch

class MainViewModel(app: Application) : AndroidViewModel(app) {
    val repo = (app as RockAtlasApp).repository

    val types: StateFlow<List<StoneType>> = repo.types.stateIn(viewModelScope, SharingStarted.Eagerly, emptyList())
    val typeMap: StateFlow<Map<String, StoneType>> =
        repo.types.map { l -> l.associateBy { it.id } }.stateIn(viewModelScope, SharingStarted.Eagerly, emptyMap())
    val stones: StateFlow<List<Stone>> = repo.stones.stateIn(viewModelScope, SharingStarted.Eagerly, emptyList())
    val images: StateFlow<Map<String, CachedImage>> = repo.images.stateIn(viewModelScope, SharingStarted.Eagerly, emptyMap())
    val favorites: StateFlow<Set<String>> = repo.favoriteIds.stateIn(viewModelScope, SharingStarted.Eagerly, emptySet())

    init {
        viewModelScope.launch { runCatching { repo.ensureSeeded() } }
    }

    fun requestImage(stoneId: String) {
        viewModelScope.launch { runCatching { repo.ensureImage(stoneId) } }
    }

    fun toggleFavorite(stoneId: String) {
        val isFav = stoneId in favorites.value
        viewModelScope.launch { repo.toggleFavorite(stoneId, isFav) }
    }
}
