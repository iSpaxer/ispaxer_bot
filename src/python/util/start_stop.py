from typing import Any

from aiogram import Bot
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, AsyncSession

from src.python.db.engine import create_db


async def startup(
        async_engine: AsyncEngine,
        async_session: async_sessionmaker[AsyncSession],
        bot: Bot
) -> Any:
    await create_db()


async def shutdown() -> Any:
    print("Бот лёг")