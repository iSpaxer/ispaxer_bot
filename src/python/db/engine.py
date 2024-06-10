from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.python.config import settings_db
from src.python.db.base import Base

# Соединение с PostgreSQL Database
engine = create_async_engine(
    url=settings_db.DB_URL_ASYNCPG,
    echo=True
)

session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
