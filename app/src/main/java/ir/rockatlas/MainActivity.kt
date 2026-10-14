package ir.rockatlas

import android.net.Uri
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.activity.viewModels
import androidx.compose.foundation.layout.padding
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.outlined.CameraAlt
import androidx.compose.material.icons.outlined.Map
import androidx.compose.material.icons.outlined.MenuBook
import androidx.compose.material.icons.outlined.Search
import androidx.compose.material3.Icon
import androidx.compose.material3.NavigationBar
import androidx.compose.material3.NavigationBarItem
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.navigation.NavGraph.Companion.findStartDestination
import androidx.navigation.NavHostController
import androidx.navigation.NavType
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.currentBackStackEntryAsState
import androidx.navigation.compose.rememberNavController
import androidx.navigation.navArgument
import ir.rockatlas.ui.AboutScreen
import ir.rockatlas.ui.AtlasScreen
import ir.rockatlas.ui.IdentifyScreen
import ir.rockatlas.ui.IntroScreen
import ir.rockatlas.ui.MainViewModel
import ir.rockatlas.ui.RegionsScreen
import ir.rockatlas.ui.RockAtlasTheme
import ir.rockatlas.ui.SearchScreen
import ir.rockatlas.ui.StoneDetailScreen
import ir.rockatlas.ui.TypeScreen

private data class Tab(val route: String, val label: String, val icon: ImageVector)

private val tabs = listOf(
    Tab("atlas", "اطلس", Icons.Outlined.MenuBook),
    Tab("search", "جستجو", Icons.Outlined.Search),
    Tab("identify", "شناسایی", Icons.Outlined.CameraAlt),
    Tab("regions", "مناطق", Icons.Outlined.Map),
)

class MainActivity : ComponentActivity() {
    private val vm: MainViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            RockAtlasTheme {
                var showIntro by rememberSaveable { mutableStateOf(true) }
                if (showIntro) {
                    IntroScreen(onDone = { showIntro = false })
                    return@RockAtlasTheme
                }
                val nav = rememberNavController()
                val entry by nav.currentBackStackEntryAsState()
                val route = entry?.destination?.route?.substringBefore('?')
                Scaffold(
                    bottomBar = {
                        NavigationBar {
                            tabs.forEach { tab ->
                                NavigationBarItem(
                                    selected = route == tab.route,
                                    onClick = { nav.goTab(tab.route) },
                                    icon = { Icon(tab.icon, null) },
                                    label = { Text(tab.label) },
                                )
                            }
                        }
                    },
                ) { pad ->
                    NavHost(nav, startDestination = "atlas", modifier = Modifier.padding(bottom = pad.calculateBottomPadding())) {
                        val openStone: (String) -> Unit = { nav.navigate("stone/${Uri.encode(it)}") }
                        val openType: (String) -> Unit = { nav.navigate("type/${Uri.encode(it)}") }
                        composable("atlas") {
                            AtlasScreen(vm, onType = openType, onFavorites = { nav.navigate("search?fav=true") }, onAbout = { nav.navigate("about") })
                        }
                        composable(
                            "search?country={country}&fav={fav}",
                            arguments = listOf(
                                navArgument("country") { type = NavType.StringType; nullable = true; defaultValue = null },
                                navArgument("fav") { type = NavType.BoolType; defaultValue = false },
                            ),
                        ) { e ->
                            SearchScreen(vm, e.arguments?.getString("country"), e.arguments?.getBoolean("fav") ?: false, openStone)
                        }
                        composable("identify") {
                            IdentifyScreen(vm, onStone = openStone, onSearch = { nav.goTab("search") })
                        }
                        composable("regions") { RegionsScreen(vm, openStone) }
                        composable("about") { AboutScreen(onBack = { nav.popBackStack() }) }
                        composable("type/{id}") { e ->
                            TypeScreen(vm, e.arguments?.getString("id").orEmpty(), openStone, onBack = { nav.popBackStack() })
                        }
                        composable("stone/{id}") { e ->
                            StoneDetailScreen(
                                vm, e.arguments?.getString("id").orEmpty(),
                                onBack = { nav.popBackStack() },
                                onType = openType,
                                onCountry = { nav.navigate("search?country=${Uri.encode(it)}") },
                            )
                        }
                    }
                }
            }
        }
    }
}

private fun NavHostController.goTab(route: String) {
    navigate(route) {
        popUpTo(graph.findStartDestination().id) { saveState = true }
        launchSingleTop = true
        restoreState = true
    }
}
