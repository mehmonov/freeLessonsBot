from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tartib = [
    '1-dars',
    '2-dars',
    '3-dars',
    '4-dars',
    '5-dars',
    '6-dars',
    '7-dars',
    '8-dars',
    '9-dars',
    '10-dars',
]

tartib.sort()
menu = ReplyKeyboardMarkup(row_width=3)
for key in tartib:
    menu.insert(KeyboardButton(text=key))
    
menu.insert(KeyboardButton(text='Bosh menuya'))


# menu = ReplyKeyboardMarkup(
#     keyboard = [
#         [
#             KeyboardButton(text='Kompyuter savodxonligi'),
#             KeyboardButton(text='Microsoft Office darslari'),
#         ],
#     ],
#     resize_keyboard=True
# )