import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommandScopeAllPrivateChats

from config import *
from db.engine import *
from middleware import DbSessionMiddleware
from src.python.rabbitmq import aio_rabbit
from src.python.router.advice.advice_router import advice_router
from src.python.router.group import group_routers
from src.python.router.private import private_routers
from src.python.util import startup, shutdown
from src.python.util.commands_for_router import all_botCommand

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)

async def main():
    # await aio_rabbit.main()

    # bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)

    bot.list_admins = []
    dp = Dispatcher(storage=MemoryStorage())

    rabbit_mq_connection = asyncio.create_task(aio_rabbit.main(bot, dp))

    #### include Private chat router ########
    for pr_router in private_routers:
        dp.include_router(pr_router)

    #### include Group and Supergroup chat router ########
    for gr_router in group_routers:
        dp.include_router(gr_router)


    #### include other pouters ########
    dp.include_routers(advice_router)

    dp["async_engine"] = engine
    dp["async_session"] = session_maker

    dp.startup.register(startup)
    dp.shutdown.register(shutdown)

    dp.update.middleware.register(DbSessionMiddleware(session_pool=session_maker))
    await bot.delete_my_commands(scope=BotCommandScopeAllPrivateChats()) # удаление кнопки меню
    await bot.set_my_commands(commands=all_botCommand, scope=BotCommandScopeAllPrivateChats()) # вставка кнопки меню
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


# async def start():
#     t1 = asyncio.create_task(main())
#     t2 = asyncio.create_task(aio_rabbit.main())
#     await t2
#     await t1


if __name__ == "__main__":
    asyncio.run(main())
