from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message

from src.python.keyboard import inline
from src.python.router.payment.product import Product
from src.python.static import dino_stickers
from src.python.util.commands_for_router import cmd_pay

command_payment_router = Router(name="command_payment_router")


@command_payment_router.message(Command(cmd_pay))
async def cmd_pay(message: Message, bot: Bot):
    await message.answer_sticker(sticker=dino_stickers.HAPPINESS)
    await message.answer(
        text="Выберете какой продукт вы хотите купить",
        reply_markup=inline.get_callback_btns(
            btns={
                "MacBook Air 13 2021": f"buy_{Product.MacBook_Air_13_2021}",
                "MacBook Air 15 2022": f"buy_{Product.MacBook_Air_15_2023}",
            }
        )
    )


