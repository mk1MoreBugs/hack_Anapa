package data

import data.client.RequestResponse
import data.client.Routers
import data.models.BookingIn
import data.models.BookingOut
import data.models.Organizer
import data.models.Platform
import io.ktor.client.call.*

class Repository : IRepository {
    private val request = RequestResponse()
    override suspend fun readAllPlatforms(address: String?): List<Platform> = request.getRequest(
        route = Routers.PLATFORMS.url.plus(address),
        nameParameter = "address",
        valueParameter = address,
    ).body()

    override suspend fun createPlatform(platform: Platform): Int = request.postRequest(
        route = Routers.PLATFORMS.url,
        data = platform
    ).status.value

    override suspend fun readPlatformsWithPrice(priceUp: Int, priceDown: Int): List<Platform> = request.getRequest(
        route = Routers.PLATFORMS.url,
        nameParameter = "price-up",
        valueParameter = priceDown.toString(),
    ).body()

    override suspend fun readOrganizers(): List<Organizer> = request.getRequest(
        route = Routers.ORGANIZER.url,
    ).body()

    override suspend fun createOrganizer(organizer: Organizer): Int = request.postRequest(
        route = Routers.ORGANIZER.url,
        data = organizer,
    ).status.value

    override suspend fun readOrganizersById(organizerId: Int): List<Organizer> = request.getRequest(
        route = Routers.PLATFORMS.url,
        nameParameter = "organizer-id",
        valueParameter = organizerId.toString(),
    ).body()

    override suspend fun readAllBookings(): List<BookingOut> = request.getRequest(
        route = Routers.BOOKING.url,
    ).body()

    override suspend fun createBooking(booking: BookingIn): Int = request.postRequest(
        route = Routers.ORGANIZER.url,
        data = booking,
    ).status.value
}
