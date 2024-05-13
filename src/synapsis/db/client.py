from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from os import getenv


def init_async_db(pool_size=10, max_overflow=10) -> AsyncEngine:
    """Returns the db client"""
    user = getenv("DB_USER")
    password = getenv("DB_PASSWORD")
    host = getenv("DB_HOST")
    port = getenv("DB_PORT")
    database = getenv("DB_NAME")

    return create_async_engine(
        f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}",
        pool_size=pool_size,
        max_overflow=max_overflow,
    )
