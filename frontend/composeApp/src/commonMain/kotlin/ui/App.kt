package ui

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.material.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import org.jetbrains.compose.ui.tooling.preview.Preview


@Composable
@Preview
fun App() {
    MaterialTheme {

        var tabState by remember { mutableStateOf(0) }
        val titles = listOf("Площадки", "Организаторы", "Запланированные мероприятия")

        Column(Modifier.fillMaxWidth(), horizontalAlignment = Alignment.CenterHorizontally) {
            TabRow(selectedTabIndex = tabState) {
                titles.forEachIndexed { index, title ->
                    Tab(
                        text = { Text(title) },
                        selected = tabState == index,
                        onClick = { tabState = index }
                    )
                }
            }
            if (tabState == 0) {
                Platfofms()
            } else if (tabState == 1) {
                Organizer()
            } else {
                Booking()
            }
        }
    }
}
