package data.models

data class BookingIn(
    val platform: Platform,
    val booking: BookingOut,
    val organizer: Organizer,
)
