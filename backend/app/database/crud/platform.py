from sqlmodel import select
from sqlmodel import Session

from app.database.models.platform import Platform


def create_platform(session: Session, platform: Platform):
    session.add(platform)
    session.commit()


def read_all_platform(session: Session):
    stmt = select(Platform).order_by(Platform.id)
    return session.scalars(stmt).all()


def read_platform_by_address(session: Session, address: str):
    stmt = select(Platform).select_from(Platform).where(Platform.address == address).order_by(Platform.id)
    return session.scalars(stmt).all()


def read_platform_price_up_and_price_down(session: Session, price_up: int, price_down: int):
    stmt = select(Platform).where(Platform.price >= price_up).where(Platform.price <= price_down).order_by(Platform.id)
    return session.scalars(stmt).all()
