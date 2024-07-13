from datetime import date
from typing import Optional

from sqlmodel import Field, SQLModel, Relationship

from app.database.models.organizer import Organizer
from app.database.models.platform import Platform


class Booking(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    platform_id: int = Field(foreign_key="platform.id")
    organizer_id: str = Field(foreign_key="organizer.id")
    event_start_date: date
    event_end_date: date
    application_approved: bool

    platform: Platform = Relationship(back_populates="bookings")
    organizer: Organizer = Relationship(back_populates="bookings")
