from aiogram import Router, F
from aiogram.types import Message
from geopy.distance import geodesic as GD


from src.python.static import dino_stickers


user_data_router = Router(name="user_data_router")


@user_data_router.message(F.location)
async def get_location(message: Message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    print(f"latitude={latitude}; longitude={longitude}" )
    my_location = (56.281653,44.080993)
    distance = round(GD((latitude, longitude), my_location).meters, 1)
    print(f"Расстояние от Вас, до разработчика: {distance}")
    await message.answer_sticker(stickers.DEVELOPER)
    await message.answer(f"Расстояние от Вас, до разработчика: {distance}м." )



@user_data_router.message(F.contact)
async def get_phone(message: Message):
    print(message.contact)
    await message.answer_sticker(stickers.OK)
    await message.answer(f"Красивый номер!)")