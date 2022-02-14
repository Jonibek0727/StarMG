from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp

contact_btn_default = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱", request_contact=True),
        ],
    ],
    resize_keyboard=True
)

