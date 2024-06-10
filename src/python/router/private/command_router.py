import traceback

from aiogram import Router, F, Bot
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from src.python.keyboard import reply, inline
from src.python.service.CommandService import CommandService
from src.python.static import stickers
from src.python.util.commands_for_router import cmd_del_kb, cmd_id, cmd_share, cmd_register, cmd_inline

router = Router(name="command_router")


@router.message(CommandStart())
async def cmd_start(message: Message, bot: Bot):
    await message.answer_sticker(stickers.HELLO)
    print(message.from_user.first_name)
    await message.answer(f"Привет,  {message.from_user.first_name}")
    # await message.answer_sticker(stickers.CRY)


@router.message(Command(cmd_del_kb))
async def cmd_del_kb(message: Message):
    await message.answer_sticker(stickers.CRINGE)
    await message.answer("Ну окэй...", reply_markup=reply.del_kb)


@router.message(Command(cmd_id))
async def cmd_id(message: Message):
    await message.answer(f"Твой ID: {message.from_user.id}")


@router.message(Command(cmd_share))
async def cmd_share(message: Message):
    await message.answer_sticker(stickers.THOUGHT)
    await message.answer(
        text="Выбирайте чем хотите поделиться со мной!",
        reply_markup=reply.kb_share.as_markup(
            resize_keyboard=True,

            input_field_placeholder="Поделиться"
        )
    )


# @router.message(Command(cmd_inline))
# async def cmd_inline(message: Message):
#     await message.answer(
#         text="Отправляю inline кнопку!",
#         reply_markup=inline.get_callback_btns(
#             btns={
#                 'Первая': 'first',
#                 'Вторая': 'second'
#             }
#         )
#     )

@router.message(Command(cmd_inline))
async def cmd_inline(message: Message):
    await message.answer(
        text="Отправляю inline кнопку!",
        reply_markup=inline.first()
    )


@router.message(Command(cmd_register))
async def cmd_register(message: Message, session: AsyncSession):
    try:
        await CommandService.register(message, session)
        await message.answer_sticker(sticker=stickers.HELLO)
        await message.answer(text=f"Привет, {message.from_user.full_name}! Твой аккаунт был зарегистрирован!")
    except Exception as e:
        traceback.print_exc()
        await message.answer_sticker(sticker=stickers.CRY)
        await message.answer(f"Ошибка сохранения данных!")
