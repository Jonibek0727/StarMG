from unicodedata import name
from aiogram import types
from aiogram.types import Message, ReplyKeyboardRemove
# from matplotlib.pyplot import text
# from telegram import CallbackQuery, Message
from aiogram.types import Message, CallbackQuery
from keyboards.default.star_mig import menu
from keyboards.inline.contactinline import contact_btn
from states.sorov import SorovNoma
from aiogram.dispatcher import FSMContext
from keyboards.default.sorov_btn import kun_kech, on_off, paynet
from keyboards.default.contact import contact_btn_default
from aiogram import Bot, Dispatcher, executor, types
from loader import dp, bot
import re
from aiogram.dispatcher.filters import Command
from filters import IsPrivate


# bot = Bot(token="5150485516:AAHIwMI6qQ0GaozfzaSSUEDALj0UghOmAYA")

PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'

@dp.callback_query_handler(text="lan_uz")
async def lanuz(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Bo'limlardan birini tanlang", reply_markup = menu)


@dp.message_handler(IsPrivate(), text="📞 Contact")
async def con(message: Message):
    await types.ChatActions.upload_photo()
    text = 'Siz Avto star MIG jamoasi bilan bog\'laning'
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('media/foto/photo_2022-01-30_20-34-54.jpg'), text)
    await message.answer_media_group(media)
    await message.answer('Boglanish uchun',reply_markup = contact_btn)
    

@dp.message_handler(IsPrivate(), text="📝 RO'YHATDAN O'TISH")
async def con(message: Message):
    await message.answer("Siz Ro'yxatdan o'tish bo'limini tanladingiz.\nIltimos To'liq ism familiyangizni kiriting\nva telegramdagi niknameizni jo'nating:", reply_markup= ReplyKeyboardRemove())
    await SorovNoma.fullname.set()

@dp.message_handler(IsPrivate(), state=SorovNoma.fullname)
async def FISH(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data(
        {"name":fullname}
    )
    await message.answer("Telefon raqamingizni kiriting to'liq kod orqali:👇", reply_markup=contact_btn_default)
    await SorovNoma.Tell.set()

@dp.message_handler(IsPrivate(), state=SorovNoma.Tell, content_types="contact")
async def TELL(message: types.Message, state: FSMContext):
    tell = message
   
    if "text" in tell:
        if (re.search(PHONE_NUM,tell)):
            await state.update_data(
                {"Tel":tell}
            
            )
            await message.answer("Pasport seriya va raqam :", reply_markup= ReplyKeyboardRemove())
            await SorovNoma.PS.set()
        else:
            await message.answer("Siz tergan raqam tarmoqda mavjud emas iltimos qaytadan urunib ko'ring\n misol uchun +998901234567")
            await SorovNoma.tell.set()
    elif "phone_number" in tell.contact:
        if (re.search(PHONE_NUM,tell.contact.phone_number)):
            await state.update_data(
                {"Tel":tell.contact.phone_number}
            
            )
            await message.answer("Pasport seriya va raqam :", reply_markup= ReplyKeyboardRemove())
            await SorovNoma.PS.set()
        else:
            await message.answer("Siz tergan raqam tarmoqda mavjud emas iltimos qaytadan urunib ko'ring\n misol uchun +998901234567")
            await SorovNoma.tell.set()

    



@dp.message_handler(IsPrivate(), state=SorovNoma.PS)
async def pasport(message: types.Message, state: FSMContext):
    PS = message.text
    await state.update_data(
        {"Ps":PS}
    )
    await message.answer("Doimiy yashash manzilini kiriting 🏠:")
    await SorovNoma.JSHR.set()



@dp.message_handler(IsPrivate(), state=SorovNoma.JSHR)
async def JSHR(message: types.Message, state: FSMContext):
    Jshr = message.text
    await state.update_data(
        {"Jshr":Jshr}
    )
    await message.answer("Ta'lim yo'nalishlardan birini tanlang:", reply_markup=kun_kech)
    await SorovNoma.Talim_yunalish.set()



@dp.message_handler(IsPrivate(), state=SorovNoma.Talim_yunalish)
async def Talim_yon(message: types.Message, state: FSMContext):
    talim = message.text
    await state.update_data(
        {"talim":talim}
    )
    await message.answer("Online yoki offline", reply_markup=on_off)
    await SorovNoma.on_of.set()



@dp.message_handler(IsPrivate(), state=SorovNoma.on_of)
async def Online(message: types.Message, state: FSMContext):
    on_off = message.text
    await state.update_data(
        {"on_off":on_off}
    )
    await message.answer("To'lov necha foizda to'laysiz", reply_markup=paynet)
    await SorovNoma.Paynet.set()



@dp.message_handler(IsPrivate(), state=SorovNoma.Paynet)
async def Payne(message: types.Message, state: FSMContext):
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

    msg = f'ISM: {name}\n'
    msg += f'Tell: {Tel}\n'
    msg += f'Pasporport seia va raqam: {Ps}\n'
    msg += f'JSHR raqam: {JSH}\n'
    msg += f'Talim turi: {Talim}\n'
    msg += f'Online/offline: {On_off}\n'
    msg += f'Tulov miqdori: {Paynet}\n'


    await message.answer("Raxmat sizning ma'lumotlaringiz qabul qilindi", reply_markup=menu)
    await message.answer(msg)
    await bot.send_message(-768512574, msg)
    await state.finish()


