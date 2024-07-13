from sqlmodel import Session, select

from app.database import BookingInDB, Platform, Organizer


def create_booking(session: Session, booking: BookingInDB):
    session.add(booking)
    session.commit()


def read_bookings(session: Session):
    stmt = select(
        Platform,
        BookingInDB,
        Organizer,
    ).select_from(
        BookingInDB
    ).join(
        Platform
    ).join(
        Organizer
    ).order_by(
        BookingInDB.id
    )
    return session.exec(stmt)
