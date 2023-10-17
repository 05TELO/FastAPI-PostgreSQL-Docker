from typing import Annotated, AsyncGenerator

from fastapi import Depends
from sqlalchemy import engine as eng
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import async_sessionmaker
from app.config_data.config import load_config
from app.config_data.dirs import DIR_REPO

conf = load_config(str(DIR_REPO / ".env"))
db_url = eng.URL.create(
    drivername=conf.postgresql.driver,
    username=conf.postgresql.user,
    password=conf.postgresql.pas,
    host=conf.postgresql.host,
    port=conf.postgresql.port,
    database=conf.postgresql.db,
)

engine = create_async_engine(db_url)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


Base = declarative_base()


async def get_session() -> AsyncGenerator:
    async with async_session() as session:
        yield session


db_dependency = Annotated[AsyncSession, Depends(get_session)]
