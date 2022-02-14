from unicodedata import name
from aiogram import types
from aiogram.types import Message, ReplyKeyboardRemove
# from matplotlib.pyplot import text
# from telegram import CallbackQuery, Message
from aiogram.types import Message, CallbackQuery
from keyboards.default.star_mig_ru import  menu_rus
from keyboards.inline.contact_rus import contact_btn_rus
from states.state_rus import SorovNoma_rus
from aiogram.dispatcher import FSMContext
from keyboards.default.sorov_rus import kun_kech_rus, on_off_rus, paynet_rus
from aiogram import Bot, Dispatcher, executor, types
from loader import dp
import re
from aiogram.dispatcher.filters import Command
from filters import IsPrivate


bot = Bot(token="5150485516:AAHIwMI6qQ0GaozfzaSSUEDALj0UghOmAYA")

PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'

@dp.callback_query_handler(text="lan_ru")
async def lanru(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите один из разделов", reply_markup = menu_rus)


@dp.message_handler(IsPrivate(), text="📞 КОНТАКТ")
async def conru(message: Message):
    await message.answer("Для подключения", reply_markup = contact_btn_rus)

@dp.message_handler(IsPrivate(), text="📝 РЕГИСТРАЦИЯ")
async def conrus(message: Message):
    await message.answer("Вы выбрали раздел регистрация.\nПожалуйста введите свое полное имя\nИ пришлите наш никнейм в телеграм:", reply_markup= ReplyKeyboardRemove())
    await SorovNoma_rus.fullname.set()

@dp.message_handler(IsPrivate(), state=SorovNoma_rus.fullname)
async def FISHru(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data(
        {"name":fullname}
    )
    await message.answer("Введите свой номер телефона, используя полный код:")
    await SorovNoma_rus.Tell.set()

@dp.message_handler(IsPrivate(), state=SorovNoma_rus.Tell)
async def TELLru(message: types.Message, state: FSMContext):
    tell = message.text
    if (re.search(PHONE_NUM,tell)):
        await state.update_data(
            {"Tel":tell}
        
        )
        await message.answer("ПАСПОРТ СЕРИЯ и НОМЕР :")
        await SorovNoma_rus.PS.set()
    else:
        await message.answer("Набранный вами номер недоступен в сети, попробуйте еще раз\n Например +998901234567")
        await SorovNoma_rus.tell.set()
    
    


@dp.message_handler(IsPrivate(), state=SorovNoma_rus.PS)
async def pasportru(message: types.Message, state: FSMContext):
    PS = message.text
    await state.update_data(
        {"Ps":PS}
    )
    await message.answer("JSHR:")
    await SorovNoma_rus.JSHR.set()



@dp.message_handler(IsPrivate(), state=SorovNoma_rus.JSHR)
async def JSHR(message: types.Message, state: FSMContext):
    Jshr = message.text
    await state.update_data(
        {"Jshr":Jshr}
     )
    await message.answer("Выберите одно из образовательных направлений:", reply_markup=kun_kech_rus)
    await SorovNoma_rus.Talim_yunalish.set()



@dp.message_handler(IsPrivate(), state=SorovNoma_rus.Talim_yunalish)
async def Talim_yon_ru(message: types.Message, state: FSMContext):
    talim = message.text
    await state.update_data(
        {"talim":talim}
    )
    await message.answer("Online или offline", reply_markup=on_off_rus)
    await SorovNoma_rus.on_of.set()



@dp.message_handler(IsPrivate(), state=SorovNoma_rus.on_of)
async def Online_ru(message: types.Message, state: FSMContext):
    on_off = message.text
    await state.update_data(
        {"on_off":on_off}
    )
    await message.answer("Какой процент оплаты вы платите", reply_markup=paynet_rus)
    await SorovNoma_rus.Paynet.set()



@dp.message_handler(IsPrivate(), state=SorovNoma_rus.Paynet)
async def Payne_ru(message: types.Message, state: FSMContext):
    paynet = message.text
    await state.update_data(
        {"paynet":paynet}
    )
    
    data = await state.get_data()

    name = data.get("name")
    Tel = data.get("Tel")
    Ps = data.get("Ps")
    JSH = data.get("Jshr")
    Talim = data.get("talim")
    On_off = data.get("on_off")
    Paynet = data.get("paynet")

    msg = f"ИМЯ: {name}\n"
    msg += f"ТЕЛЕФОН: {Tel}\n"
    msg += f"ПАСПОРТ СЕРИЯ И НОМЕР: {Ps}\n"
    #msg += f'JSHR raqam: {JSH}\n'
    msg += f"ТИП ОБРАЗОВАНИЯ: {Talim}\n"
    msg += f"Online/offline: {On_off}\n"
    msg += f"СУММА ПЛАТЕЖА: {Paynet}\n"
    await message.answer("СПАСИБО ВАША ИНФОРМАЦИЯ ПОЛУЧЕНА", reply_markup=menu_rus)
    await message.answer(msg)
    await bot.send_message(-768512574, msg)
    await state.finish()


