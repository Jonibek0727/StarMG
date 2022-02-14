from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp

kun_kech_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Oчная форма обучения"),
            KeyboardButton(text="вечернее образование"),
        ],
    ],
    resize_keyboard=True
)


on_off_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Online образование"),
            KeyboardButton(text="Offline образование"),
        ],
    ],
    resize_keyboard=True
)


paynet_rus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="30%"),
            KeyboardButton(text="50%"),
        ],
    ],
    resize_keyboard=True
)