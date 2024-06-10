import logging
from datetime import datetime

from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.python.keyboard.inline import get_callback_btns
from src.python.static.emodji import parse_numbers

admin_group_router = Router(name="admin_group_router")


@admin_group_router.message(CommandStart)
async def cmd_start_group(message: Message, bot: Bot):
    chat_id = message.chat.id
    print(f"chat_id {chat_id}")
    count = bot.get_chat_member_count(chat_id)
    print(f"count {count}")
    bot.admins_list = await bot.get_chat_member(chat_id)
    await message.answer(
        text=f"""
        <b>Вас приветствует бот, админки! 👋 
        Количество аутифицированных администраторов {parse_numbers(len(bot.admins_list))}.
        Последняя дата обновления администраторов: {datetime.now()} 🕗</b>
        """,
        reply_markup=get_callback_btns(
            btns={
                "♻️ Синхронизировать администраторов.": "groups_update_admins",
                "👥 Показать всех администраторов.": "groups_see_admins"
            }
        )
    )



