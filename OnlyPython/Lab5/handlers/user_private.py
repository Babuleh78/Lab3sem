
from aiogram import F, types, Router
from aiogram.filters import  CommandStart, Command, or_f

user_private_router = Router()
from klava import reply

@user_private_router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Ну здарова", reply_markup = reply.start_kb)

@user_private_router.message(or_f(Command('menu'), (F.text.lower() == 'меню')))
async def menu_command(message: types.Message):
    await message.answer("Это меню")
@user_private_router.message(Command('music'))
async def music_command(message: types.Message):
    await message.answer("Раздел с музыкой")

@user_private_router.message(F.text.lower().contains('шашик'))
async def filtr(message: types.Message):
    await message.answer("Это Никита Шашура")

@user_private_router.message()
async def ans(message: types.Message):
    await message.answer(message.text)
