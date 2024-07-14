package data.models

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable


@Serializable
data class Platform(
    val id: Int?,
    val name: String,
    val information: String,
    val address: String,
    @SerialName("platform_category")
    val platformCategory: String,
    val capacity: Int,
    val price: Int,
)