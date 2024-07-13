from typing import Annotated

from fastapi import APIRouter, Query

from app.api.dependencies import SessionDep
from app.database.crud.platform import read_all_platform, read_platform_by_address, \
    read_platform_price_up_and_price_down, create_platform
from app.database.models.platform import Platform

router = APIRouter(
    prefix="/platforms",
    tags=["platform routers"],
)


@router.get("/")
async def get_platforms(
        session: SessionDep,
        address: Annotated[str | None, Query()] = None,
) -> list[Platform]:
    if address:
        list_platforms: list[Platform] = read_platform_by_address(
            session=session,
            address=address
        )
    else:
        list_platforms: list[Platform] = read_all_platform(session)
    return list_platforms


@router.get("/price")
async def get_platforms(
        session: SessionDep,
        price_up: Annotated[int, Query()],
        price_down: Annotated[int, Query()],
) -> list[Platform]:
    list_platforms: list[Platform] = read_platform_price_up_and_price_down(
        session=session,
        price_up=price_up,
        price_down=price_down,
    )
    return list_platforms


@router.post("/")
async def create_new_platform(session: SessionDep, platform: Platform):
    create_platform(session=session, platform=platform)
