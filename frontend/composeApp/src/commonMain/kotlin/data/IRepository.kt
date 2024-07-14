package data

import data.models.BookingIn
import data.models.BookingOut
import data.models.Organizer
import data.models.Platform

interface IRepository {
    suspend fun readAllPlatforms(address: String?): List<Platform>

    suspend fun createPlatform(platform: Platform): Int

    suspend fun readPlatformsWithPrice(priceUp: Int, priceDown: Int): List<Platform>

    suspend fun readOrganizers(): List<Organizer>

    suspend fun createOrganizer(organizer: Organizer): Int

    suspend fun readOrganizersById(organizerId: Int): List<Organizer>

    suspend fun readAllBookings(): List<BookingOut>

    suspend fun createBooking(booking: BookingIn): Int
}
