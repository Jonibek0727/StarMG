from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.laguegebtn import lan_btn
from filters import IsPrivate

from loader import dp


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}!\nRo'yhatdan o'tishni xohlasangiz iltimos pastdagi buyrug'lardan birini tanlang 👇🏿", reply_markup=lan_btn)
