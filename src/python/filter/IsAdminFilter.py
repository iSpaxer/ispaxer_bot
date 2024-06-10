from typing import Any, Union, Dict

from aiogram import Bot
from aiogram.filters import Filter

__all__ = []

from aiogram.types import Message


class IsAdminFilter(Filter):
    def __init__(self):
        pass

    async def __call__(self, message: Message, bot: Bot) -> bool:
        return message.from_user.id in bot.admins_list


