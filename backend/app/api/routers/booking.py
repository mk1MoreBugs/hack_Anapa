import datetime

from fastapi import APIRouter

from app.api.dependencies import SessionDep
from app.database.models.booking import BookingInDB, BookingWithPlatformAndOrganizer
from app.database.crud.booking import create_booking, read_bookings
from app.database.models.booking import BookingIn

router = APIRouter(
    prefix="/booking",
    tags=["booking routers"],
)


@router.post("/")
async def create_new_booking(session: SessionDep, booking: BookingIn):
    save_booking_in_db = BookingInDB.model_validate(
        booking,
        update={
            "event_start_date": datetime.date.fromisoformat(booking.event_end_date),
            "event_end_date": datetime.date.fromisoformat(booking.event_end_date)
        }
    )
    create_booking(session=session, booking=save_booking_in_db)


@router.get("/")
async def route_read_bookings(session: SessionDep) -> list[BookingWithPlatformAndOrganizer]:
    list_bookings = read_bookings(session=session)
    result = []
    for item in list_bookings:
        result.append(
                BookingWithPlatformAndOrganizer(
                    platform=item[0],
                    booking=item[1],
                    organizer=item[2],
                )
        )
    return result



