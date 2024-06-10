from datetime import datetime

from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message

from src.python.keyboard.inline import get_callback_btns
from src.python.static.emodji import parse_numbers

callback_group_router = Router(name="callback_group_router")


@callback_group_router.callback_query(F.data == "groups_update_admins")
async def cbk_update_admins(callback: CallbackQuery, message: Message, bot: Bot):
    bot.admins_list = bot.get_chat_member(message.chat.id)
    await callback.message.edit_text(
        text=f"""
            <b>Вас приветствует бот, админки! 👋 
            Количество аутифицированных администраторов {parse_numbers(len(bot.admins_list))}.
            Последняя дата обновления администраторов: {datetime.now()} 🕗</b>
            """,
        reply_markup=get_callback_btns(
            btns={
                "♻️ Обновить администраторов.": "groups_update_admins",
                "👥 Показать всех администраторов.": "groups_see_admins"
            }
        )
    )
    await callback.answer("✅ Обновлено!", show_alert=True)


@callback_group_router.callback_query(F.data == "groups_see_admins")
async def cbk_see_admins(callback: CallbackQuery, message: Message, bot: Bot):
    result_text = "👥 Администраторы: "
    for admn in bot.admins_list:
        result_text += f"\n👉 {admn}"
    await callback.message.edit_text(
        text=result_text,
        reply_markup=get_callback_btns(
            btns={
                "⬅️ Назад.": "groups_update_admins"
            }
        )

    )

