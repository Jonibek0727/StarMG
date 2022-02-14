from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_rus = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="📝 РЕГИСТРАЦИЯ"),
            KeyboardButton(text="🚘 ОБ АВТОШКОЛЕ"),
            
        ],
        
        [
            KeyboardButton(text='📞 КОНТАКТ'),
        ],
       
        
    ],
    resize_keyboard=True
)