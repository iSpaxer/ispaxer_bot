from datetime import datetime

from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from src.python.db.models.user import User


class CommandService:

    def __init__(self):
        pass

    @staticmethod
    async def register(
            message: Message,
            session: AsyncSession
    ):
        await session.merge(
            User(
                id=message.from_user.id,
                username="message.from_user.username",
                # creation_date_time=datetime.now
            )
        )
        # raise ValueError("error")
        await session.flush()
