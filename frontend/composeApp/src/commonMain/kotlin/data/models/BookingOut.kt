package data.models

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable


@Serializable
data class BookingOut(
    val id: Int?,
    @SerialName("platform_id")
    val platformId: Int,
    @SerialName("organizer_id")
    val organizerId: Int,
    @SerialName("application_approved")
    val applicationApproved: Boolean,
    @SerialName("event_name")
    val eventName: String,
    @SerialName("event_start_date")
    val eventStartDate: String,
    @SerialName("event_end_date")
    val eventEndDate: String,
)
