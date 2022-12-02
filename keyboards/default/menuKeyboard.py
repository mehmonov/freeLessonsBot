from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Kompyuter savodxonligi'),
            KeyboardButton(text='Microsoft Office darslari'),
        ],
        [
            KeyboardButton(text='Grafik dizayn'),
            KeyboardButton(text='Dasturlash'),
        ],
        [
            KeyboardButton(text='Kiber-xavfsizlik darslari'),
            KeyboardButton(text='Python telegram bot'),
        ],
        
    ],
    resize_keyboard=True
)