from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# __all__ = ['reply_kb_first']

kb_share = ReplyKeyboardBuilder()
kb_share.add(
    KeyboardButton(text="📱️", request_contact=True),
    KeyboardButton(text="🛰", request_location=True)
)
kb_share.adjust(2)

del_kb = ReplyKeyboardRemove()

