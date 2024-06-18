import logging

from aiogram import Router, F, Bot, types
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery, LabeledPrice, PreCheckoutQuery, Message

from src.python.config import tg_config

callback_payment_router = Router(name="callback_payment_router")


@callback_payment_router.callback_query(F.data.startswith("buy_"))
async def buy_(callback: CallbackQuery, bot: Bot):
    obj = (callback.data.split("_")[-1]).replace("-", " ")
    logging.info(tg_config.BOT_PAY_TOKEN)
    await callback.message.answer_invoice(
        title=f"Покупка {obj}",
        description="Нажимая кнопку 'Заплатить' вы подписываете договор купли-продажи.",
        provider_token=tg_config.BOT_PAY_TOKEN,
        currency="rub",
        # start_parameter="time-machine-example",
        payload="Payment - payload",
        prices=[
            LabeledPrice(
                label=obj,
                amount=9900
            ),
            LabeledPrice(
                label="НДС",
                amount=990
            )
        ],
        max_tip_amount=500,
        suggested_tip_amounts=[100, 200, 300, 400],
        # start_parameter="ispaxer"
        provider_data=None,
        photo_url="https://iphoriya.ru/wp-content/uploads/macbook-air-2020-space-gray-front.jpg",
        photo_width=1144,
        photo_height=1144,
        request_timeout=15
    )

# способ доставки
# @callback_payment_router.message(F.query)
# async def shipping(ship_query: types.ShippingQuery):
#     await ship_query.answer(
#         ok=True,
#
#     )


# ставим проверку, например, есть ли у нас на складе данный товар
@callback_payment_router.pre_checkout_query()
async def pre_chekout_querry(pre_checkout_query: types.PreCheckoutQuery, bot: Bot):
    logging.info("bot.answer_pre_checkout_query True")
    await pre_checkout_query.answer(ok=True, error_message="Произошла ошибка, ваши деньги не списаны")


# если успешно то вызывается эта функция
@callback_payment_router.message(F.successful_payment)
async def success(message: Message):
    await message.answer(text="Успешно!")
