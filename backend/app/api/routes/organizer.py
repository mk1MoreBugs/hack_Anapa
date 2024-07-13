from typing import Annotated

from fastapi import APIRouter, Path

from app.api.dependencies import SessionDep
from app.database import Organizer
from app.database.crud.organizer import create_user_organizer, read_user_organizers, read_user_organizer_by_id

router = APIRouter(
    prefix="/organizer",
    tags=["organizer (users) routes"],
)


@router.post("/")
async def create_organizer(session: SessionDep, organizer: Organizer):
    create_user_organizer(session=session, organizer=organizer)


@router.get("/")
async def read_organizers(session: SessionDep) -> list[Organizer]:
    list_organizers = read_user_organizers(session=session)
    return list_organizers


@router.get("/{organizer_id}")
async def read_organizer(session: SessionDep, organizer_id: Annotated[int, Path()]) -> list[Organizer]:
    organizer = read_user_organizer_by_id(session=session, organizer_id=organizer_id)
    return organizer
