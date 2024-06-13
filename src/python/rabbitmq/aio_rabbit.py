import asyncio

import aio_pika
from aiogram import Bot, Dispatcher

from src.python.main import bot


async def process_message(
        message: aio_pika.abc.AbstractIncomingMessage,
) -> None:
    async with message.process():
        print("-------------------------------------------------------")
        print(message.body)
        await bot.send_message(chat_id=671835084, text=message.body)
        await asyncio.sleep(1)


async def main(bot: Bot, dp: Dispatcher):
    # Connecting with the given parameters is also possible.
    # aio_pika.connect_robust(host="host", login="login", password="password")
    # You can only choose one option to create a connection, url or kw-based params.
    connection = await aio_pika.connect_robust(
        "amqp://alex:alex@localhost/"
    )

    queue_name = "rabbit.fanout.telegram"

    # Creating channel
    channel = await connection.channel()

    # Maximum message count which will be processing at the same time.
    await channel.set_qos(prefetch_count=100)

    # Declaring queue
    queue = await channel.declare_queue(queue_name, durable=True, passive=True)

    await queue.consume(process_message)
    try:
        # Wait until terminate
        await asyncio.Future()
    finally:
        await connection.close()

    try:
        # Wait until terminate
        await asyncio.Future()
    finally:
        await connection.close()
