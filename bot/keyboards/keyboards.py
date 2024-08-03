from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

info = ReplyKeyboardMarkup(resize_keyboard=True)
i = KeyboardButton('info')
info.add(i)

send = InlineKeyboardMarkup(resize_keyboard=True)
s = InlineKeyboardButton('send', callback_data='send')
send.add(s)