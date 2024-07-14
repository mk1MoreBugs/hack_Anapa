package data.client


enum class Routers(val url: String) {
    PLATFORMS("/platforms"),
    PRICE("/price"),
    ORGANIZER("/organizer"),
    BOOKING("/booking"),
}
