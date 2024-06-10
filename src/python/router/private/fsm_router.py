from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from src.python.util.commands_for_router import cmd_add

fsm_router = Router(name="fsm_router")


class AddProduct(StatesGroup):
    name = State()
    description = State()
    price = State()
    image = State()


@fsm_router.message(StateFilter(None), Command(cmd_add))
async def cmd_add(message: Message, state: FSMContext):
    await message.answer("Введите название товара:")
    await state.set_state(AddProduct.name)


@fsm_router.message(StateFilter(AddProduct.name), F.text)
async def cmd_add(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите описание товара:")
    await state.set_state(AddProduct.description)


@fsm_router.message(StateFilter(AddProduct.description), F.text)
async def cmd_add(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer("Введите цену товара:")
    await state.set_state(AddProduct.price)


@fsm_router.message(StateFilter(AddProduct.price), F.text)
async def cmd_add(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("Введите изображение товара")
    await state.set_state(AddProduct.image)


@fsm_router.message(StateFilter(AddProduct.image), F.photo)
async def cmd_add(message: Message, state: FSMContext):
    await state.update_data(image=message.photo[-1].file_id)
    await message.answer("Товар добавлен!")
    result = await state.get_data()
    await message.answer(str(result))
    await state.clear()
