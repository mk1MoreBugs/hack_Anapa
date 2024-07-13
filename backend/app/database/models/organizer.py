from typing import Optional

from sqlmodel import Field, SQLModel, Relationship


class Organizer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    organizer_name: str

    bookings: list["BookingInDB"] = Relationship(back_populates="organizer")
