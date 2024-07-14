package data.models

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable


@Serializable
data class Organizer(
    val id: Int?,
    @SerialName("organizer_name")
    val organizerName: String,
)
