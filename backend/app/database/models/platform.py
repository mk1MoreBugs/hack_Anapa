import enum
from typing import Optional

from sqlmodel import Field, SQLModel, Relationship


class PlatformCategoryEnum(enum.Enum):
    conference_hall = "conference hall"
    restaurant = "restaurant"
    open_areas = "open areas"


class Platform(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    information: str
    address: str
    platform_category: PlatformCategoryEnum = Field(default="conference_hall")
    capacity: int
    price: int

    bookings: list["BookingInDB"] = Relationship(back_populates="platform")
