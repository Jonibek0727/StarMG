from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import dp


lan_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="UZ", callback_data="lan_uz"),
            InlineKeyboardButton(text="RU", callback_data="lan_ru"),
        ],
    ],
)

