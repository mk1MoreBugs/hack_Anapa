from sqlmodel import Session, select

from app.database import Organizer


def create_user_organizer(session: Session, organizer: Organizer):
    session.add(organizer)
    session.commit()


def read_user_organizers(session: Session):
    stmt = select(Organizer).order_by(Organizer.id)
    return session.scalars(stmt).all()


def read_user_organizer_by_id(session: Session, organizer_id: int):
    stmt = select(Organizer).where(Organizer.id == organizer_id).order_by(Organizer.id)
    return session.scalars(stmt).all()
