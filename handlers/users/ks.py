from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile
from keyboards.default.ks.ksBeginner import menu
from loader import dp, bot

@dp.message_handler(text='Kompyuter savodxonligi')
async def ks(message: types.Message):
    await message.answer('tanlang', reply_markup=menu)