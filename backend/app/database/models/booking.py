from datetime import date
from typing import Optional, Annotated

from sqlmodel import Field, SQLModel, Relationship

from app.database.models.organizer import Organizer
from app.database.models.platform import Platform


class BookingBase(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    platform_id: int = Field(foreign_key="platform.id")
    organizer_id: int = Field(foreign_key="organizer.id")
    application_approved: bool


class BookingIn(BookingBase):
    event_start_date: Annotated[str, Field(default="2024-07-13")]
    event_end_date: Annotated[str, Field(default="2024-07-13")]


class BookingInDB(BookingBase, table=True):
    event_start_date: date
    event_end_date: date

    platform: Platform = Relationship(back_populates="bookings")
    organizer: Organizer = Relationship(back_populates="bookings")


class BookingWithPlatformAndOrganizer(SQLModel):
    platform: Platform
    booking: BookingInDB
    organizer: Organizer
