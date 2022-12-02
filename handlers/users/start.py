from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menuKeyboard import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Yangicha formatdagi platformaga xush kelibsiz! Tartiblangan va yangi darslar sizni kutmoqda. Quyidagi bo'limlardan birini tanlang.", reply_markup=menu)

