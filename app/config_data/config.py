from dataclasses import dataclass
from typing import Optional

from environs import Env


@dataclass
class PostgreSqlConfig:
    db: str
    host: str
    pas: str
    port: int
    user: str
    driver: str


@dataclass
class Config:
    postgresql: PostgreSqlConfig


def load_config(path: Optional[str]) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        postgresql=PostgreSqlConfig(
            db=env.str("DB_NAME"),
            host=env.str("DB_HOST"),
            user=env.str("DB_USER"),
            pas=env.str("DB_PASS"),
            port=env.int("DB_PORT"),
            driver=env.str("DB_DRIVERNAME"),
        )
    )
