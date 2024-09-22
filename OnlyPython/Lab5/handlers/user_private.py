import asyncio
from aiogram import F, types, Router, Bot
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from klava import reply
from klava.reply import get_keyboard
user_private_router = Router()
ADMIN_ID = 1089565570
IS_ADMIN = False
IGNORE_CASE = False
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



@user_private_router.message(CommandStart())
async def start_command(message: types.Message):
    
    await message.answer("Привет! Я бот, который поможет тебе с учебой! Я могу посоветовать музыку для занятий, подсказать действенные техники для успешного обучения, придать мотивацию, а так же помогу тебе вести список дел, которые ты завершил. Давай начнем!", 
        reply_markup = reply.get_keyboard(
            "Меню",
            "Техники",
            "Поддержать дух",
            "Музыка", 
            sizes = (2, 2)

        ),
    )
#-----------------------Про техники------------------------
@user_private_router.message(or_f(Command('techniques'), (F.text.lower() == "техники")))
async def info_panel(message: types.Message):
    await message.answer("Существует несколько техник для эффективного обучения, про какую вы хотите узнать подробнее?", 
                         reply_markup= reply.get_keyboard(
                             "Помодоро",
                             "Метод '90 на 30'",
                             "Матрица Эйзенхауэра",
                             "Метод GTD",
                             sizes = (2, 2)
                         ),
    )
@user_private_router.message((F.text.lower() == 'помодоро'))
async def menu_command(message: types.Message):
    button_more = types.InlineKeyboardButton(text="Подробнее", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    button_time = types.InlineKeyboardButton(text="Засечь время")
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[button_more], [button_time]])
    await message.answer("поставьте таймер на 25 минут и в течение этого времени выполняйте работу, ни на что не отвлекаясь. После "
                          "сделайте перерыв пять минут и повторите цикл заново — продолжайте работу. Через каждые четыре цикла сделайте большой "
                           "перерыв в 30 минут. Смысл метода в том, что монотонная работа разбивается на небольшие части, и после каждой вы получаете заслуженный отдых "
                            "Так легче взяться за такие задачи, и можно выполнить их лучше", 
                            reply_markup= keyboard)
@user_private_router.callback_query()
async def process_callback_button(callback_query: types.CallbackQuery):
    if callback_query.data == "button_pressed":
        await callback_query.answer()  # Подтверждаем нажатие кнопки
        await callback_query.message.answer('Кнопка была нажата!')

@user_private_router.message((F.text.lower() == 'засесь время'))
async def pomodoro(message: types.Message):
    await message.answer("Цикл начался! Занимайтесь 25 минут. Не забудьте взять большой перерыв после 4-х циклов")
    while True:
        await message.answer("Прошло 25 минут! Не забывайте делать перерыв.")
        await asyncio.sleep(25)
@user_private_router.message(or_f(Command('menu'), (F.text.lower() == 'меню')))
async def menu_command(message: types.Message):
    await message.answer("СыЭ")
@user_private_router.message(F.text.lower().contains('шашик'))
async def filtr(message: types.Message):
    await message.answer("Это Никита Шашура")
@user_private_router.message(Command("admin"))
async def get_admins(message: types.Message, bot: Bot):
    IsAdmin = True

#---------Для админа, если оно вообще будет. SHATTEREDDD
ADMIN_KB = get_keyboard(
    "Добавить товар",
    "Изменить товар",
    "Удалить товар",
    "Я так, просто посмотреть зашел",
    placeholder="Выберите действие",
    sizes=(2, 1, 1),
)

@user_private_router.message(Command("admin"))
async def admin_panel(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("Вы администратор! Выберите опцию:", reply_markup= ADMIN_KB)
        IS_ADMIN = True
    else:
        await message.answer("У вас нет прав администратора.")
#--------------------Пасхалски для самых маленьких-------------------
@user_private_router.message(F.text == "1602")
async def menu_command(message: types.Message):
    await message.answer("Great trial is coming :)")