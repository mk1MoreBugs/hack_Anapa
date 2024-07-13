from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from app.database.database import create_db_engine


SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlite.db"


engine = create_db_engine(
    database_url=SQLALCHEMY_DATABASE_URL,
)


def session_db():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(session_db)]
