from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy import engine as eng
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

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

engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
