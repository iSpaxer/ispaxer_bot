from aiogram.types import BotCommand

cmd_start = "start"
cmd_del_kb = "del_kb"
cmd_id = "id"
cmd_share = "share"
cmd_register = "register"
cmd_inline = "inline"
cmd_add = "add"

all_botCommand = [
    BotCommand(command=cmd_start, description="Стартовая команда."),
    BotCommand(command=cmd_del_kb, description="Удалить клавиатуру"),
    BotCommand(command=cmd_id, description="Получить свой id."),
    BotCommand(command=cmd_share, description="Поделиться информацией"),
    BotCommand(command=cmd_register, description="Зарегистрироваться в боте"),
    BotCommand(command=cmd_inline, description="Получить инлайн кнопки"),
    BotCommand(command=cmd_add, description="Добавить товар"),
]