from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp

kun_kech = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kunduzgi ta'lim"),
            KeyboardButton(text="Kechki ta'lim"),
        ],
    ],
    resize_keyboard=True
)


on_off = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Online ta'lim"),
            KeyboardButton(text="Offline ta'lim"),
        ],
    ],
    resize_keyboard=True
)


paynet = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="30%"),
            KeyboardButton(text="50%"),
        ],
    ],
    resize_keyboard=True
)