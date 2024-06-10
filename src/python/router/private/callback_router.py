from aiogram import Router, F
from aiogram.types import CallbackQuery

callback_router = Router(name="callback_router")


@callback_router.callback_query(F.data == "key1")
async def handl_query(callback: CallbackQuery):
    await callback.answer("Обработано!")
    await callback.message.answer("Выкидываю текст")


@callback_router.callback_query(F.data == "key2")
async def handl_query(callback: CallbackQuery):
    await callback.answer("Обработано!", show_alert=True)
    await callback.message.answer("Выкидываю текст")
    # logging.(callback.data)
