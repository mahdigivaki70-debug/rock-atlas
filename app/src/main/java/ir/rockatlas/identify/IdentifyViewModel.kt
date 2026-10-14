package ir.rockatlas.identify

import android.app.Application
import android.graphics.Bitmap
import android.net.Uri
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import ir.rockatlas.RockAtlasApp
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.first
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

data class IdentifyState(
    val bitmap: Bitmap? = null,
    /** FileProvider URI of the cleaned, metadata-free copy; used for sharing to Lens. */
    val imageUri: Uri? = null,
    val tests: FieldTests = FieldTests(),
    val results: List<Match> = emptyList(),
    val busy: Boolean = false,
    /** The picked file could not be read as an image. */
    val badImage: Boolean = false,
    val modelLoaded: Boolean = false,
)

class IdentifyViewModel(app: Application) : AndroidViewModel(app) {
    private val repo = (app as RockAtlasApp).repository
    private val _state = MutableStateFlow(IdentifyState())
    val state: StateFlow<IdentifyState> = _state

    private var features: ImageFeatures? = null
    private var modelScores: Map<String, Float>? = null
    private val classifier by lazy { StoneClassifier.load(app) }

    /** Last camera target, kept here so it survives the activity being recreated. */
    var pendingCaptureUri: Uri? = null

    fun onImage(source: Uri) {
        _state.update { it.copy(busy = true, badImage = false) }
        viewModelScope.launch {
            val ctx = getApplication<Application>()
            val imported = withContext(Dispatchers.IO) { ImageIO.importImage(ctx, source) }
            if (imported == null) {
                _state.update { it.copy(busy = false, badImage = true) }
                return@launch
            }
            val (bmp, uri) = imported
            withContext(Dispatchers.Default) {
                features = ColorAnalyzer.analyze(bmp)
                modelScores = classifier?.classify(bmp)
            }
            withContext(Dispatchers.IO) { ImageIO.cleanup(ctx, uri) }
            _state.update { it.copy(bitmap = bmp, imageUri = uri, modelLoaded = classifier != null) }
            rank()
        }
    }

    fun setTests(tests: FieldTests) {
        _state.update { it.copy(tests = tests) }
        if (features != null) viewModelScope.launch { rank() }
    }

    private suspend fun rank() {
        val f = features ?: return
        val stones = repo.stones.first()
        val types = repo.types.first().associateBy { it.id }
        val results = withContext(Dispatchers.Default) {
            Identifier.rank(f, _state.value.tests, stones, types, modelScores)
        }
        _state.update { it.copy(results = results, busy = false) }
    }

    fun reset() {
        features = null
        modelScores = null
        _state.value = IdentifyState()
    }
}
