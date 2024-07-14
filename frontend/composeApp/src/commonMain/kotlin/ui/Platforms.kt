package ui

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import data.Repository
import data.models.Platform
import kotlinx.coroutines.flow.StateFlow


@Composable
fun Platfofms(
    repository: Repository = Repository()
) {

    LazyColumn (
        modifier = Modifier.fillMaxSize(),
    ) {
        Text("Platforms")
    }

}

data class uiState(
    val platforms: List<Platform> = listOf()
)

