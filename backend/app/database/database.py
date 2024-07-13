from sqlalchemy import create_engine, Engine

from sqlmodel import SQLModel


def create_db_table(engine: Engine):
    SQLModel.metadata.create_all(engine)


def create_db_engine(database_url: str):
    engine = create_engine(database_url)
    create_db_table(engine)
    return engine
