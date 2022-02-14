from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="📝 RO'YHATDAN O'TISH"),
            KeyboardButton(text="🚘 AVTO MAKTAB HAQIDA"),
            
        ],
        
        [
            KeyboardButton(text='📞 Contact'),
        ],
       
        
    ],
    resize_keyboard=True
)