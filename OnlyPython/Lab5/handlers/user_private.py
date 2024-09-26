import asyncio
import os
import random
import sqlite3
from aiogram import F, types, Router, Bot
from aiogram.filters import CommandStart, Command, or_f
from klava import reply, inline
from klava.reply import get_keyboard
user_private_router = Router()
path_mas = ['C:\images\DIO.jpg', "C:\images\Megaded.png", "C:\images\Lemmi.jpg",   "C:\images\Phil.jpg",  "C:\images\Bruce.jpg",]
citata_mas= ['Музыканты моего поколения — живой пример того, чего можно достичь при наличии веры в свое правое дело, и мы пришли сюда, чтобы сказать другим: «Не сдавайтесь!»',
             '– У доктора не было права так со мной разговаривать. Я не собираюсь позволять кому-то вроде него посылать во вселенную слова, которые не соответствуют действительности обо мне. В моей реальности, когда он говорил эти вещи, они были неправдой для меня, и я не собирался это принимать. Дэйв Мастейн о диагнозе, не позволяющему ему играть ', 
             'Быть быстрым и злым недостаточно - необходимо быть быстрым и злым ублюдком и тогда люди полюбят тебя',
             'Не стоит недооценивать пацана, но если вы это делаете, то вы, ***** [черт возьми], полный ***** [нехороший человек]. Потому что этот пацан — это я.',
             'Есть только 2 категории музыки: метал и х***я [ерунда].'
             ]
ADMIN_ID = os.getenv('ADMIN')
IS_ADMIN = False
IGNORE_CASE = False
bot = Bot(token = os.getenv('TOKEN'))
def delete_ach():
    conn = sqlite3.connect('achs.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM achs''')  
    conn.commit()  
    conn.close()  
def create_db():
    conn = sqlite3.connect('achs.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS achs (
            id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            ach TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
def save_ach(user_id, message):
    conn = sqlite3.connect('achs.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO achs (user_id, ach) VALUES (?, ?)
    ''', (user_id, message))
    conn.commit()
    conn.close()
def get_ach(user_id):
    conn = sqlite3.connect('achs.db')
    cursor = conn.cursor()
    cursor.execute('SELECT ach FROM achs WHERE user_id = ?', (user_id,))
    messages = cursor.fetchall()
    conn.close()
    return messages

create_db()
#------------------------Общее-----------------
@user_private_router.message(or_f(CommandStart(), (F.text.lower() == "назад")))
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот 🤖, который поможет тебе с учебой!🧠 Я могу посоветовать музыку 🎵 для занятий, подсказать действенные техники для успешного обучения 🖥️, придать мотивацию, а так же помогу тебе вести список дел, которые ты завершил 📂 Давай начнем!", 
        reply_markup = reply.get_keyboard(
            "Мои достижения",
            "Техники",
            "Поддержать дух",
            "Музыка", 
            sizes = (2, 2)

        ),
    )
#------------Про достижения SQL и прочие страшилки-----------------------
@user_private_router.message(or_f(Command('ach'), (F.text.lower() == "мои достижения")))
async def info_panel(message: types.Message):
    await message.answer("Выбери, что ты хочешь сделать. Если хочешь внести дело, напиши его в следующем формате 'Д:Спас кота' 📚", 
                         reply_markup= reply.get_keyboard(
                             "Посмотреть список 😎",
                             "Очистить список ❌ ",
                             "Назад ↓",
                             sizes = (2, 2)
                         ),
    )

@user_private_router.message(F.text.lower().contains("д:"))
async def info_panel(message: types.Message):
    str = message.text[2:]
    save_ach(message.from_user.id, str)
    await message.answer("Ваше дело занесено!✅")

@user_private_router.message(F.text.lower() == 'очистить список')
async def info_panel(message: types.Message):
    delete_ach()
    await message.answer("Список достижений очищен!❌")
@user_private_router.message(F.text.lower() == 'посмотреть список')
async def info_panel(message: types.Message):
    user_id = message.from_user.id
    messages = get_ach(user_id)
    if messages:
        response = "Ваши дела: \n"
        for msg in messages:
            response += f"{msg[0]} \n"
    else:
        response = "Вы пока ничего не сделали🖕"

    await message.answer(response)
#----------------------Про мотивацию--------------------------------
@user_private_router.message(or_f(Command("quote"), (F.text.lower() == "поддержать дух")))
async def info_panel(message: types.Message):
    a = random.randint(0, 4)
    try:
        file_path = path_mas[a]
        photo = types.FSInputFile(path = file_path)
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
        await bot.send_message(message.chat.id, text = citata_mas[a])
    except FileNotFoundError:
        await bot.send_message(message.chat.id, "Изображение не найдено.")
    except Exception as e:
        await bot.send_message(message.chat.id, f"Произошла ошибка: {e}")
#-----------------------Про техники------------------------
@user_private_router.message(or_f(Command('techniques'), (F.text.lower() == "техники")))
async def info_panel(message: types.Message):
    await message.answer("Существует несколько техник для эффективного обучения 🌶️ про какую вы хотите узнать подробнее? 🤔", 
                         reply_markup= reply.get_keyboard(
                             "Помодоро",
                             "Метод '90 на 30'",
                             "Матрица Эйзенхауэра",
                             "Метод GTD",
                             "Назад ",
                             sizes = (2, 2)
                         ),
    )

@user_private_router.message((F.text.lower() == 'помодоро'))
async def menu_command(message: types.Message):
    await message.answer("Поставьте таймер на 25 минут и в течение этого времени выполняйте работу, ни на что не отвлекаясь. После "
                          "сделайте перерыв 5 минут и повторите цикл заново — продолжайте работу. Через каждые четыре цикла делайте большой "
                           "перерыв в 30 минут. Смысл метода в том, что монотонная работа разбивается на небольшие части, и после каждой вы получаете заслуженный отдых "
                            "Так легче взяться за такие задачи, и можно выполнить их лучше", 
                            reply_markup= inline.get_inlineMix_btns(
                                btns = {
                                    'Засечь': 'time1',
                                    'Подробнее': 'https://skillbox.ru/media/management/pomodoro/'
                                }
                            )
    )
    
@user_private_router.message((F.text.lower() == "метод '90 на 30'"))
async def menu_command(message: types.Message):
    await message.answer("По этому методу на работу отводится полтора часа (90 минут), а после — полчаса на отдых. После этого цикл повторяется."
                         " Каждый полный цикл занимает два часа."
                        "Важно: первые циклы отводите на самые важные и сложные дела, а следующие – на менее важные", 
                            reply_markup= inline.get_inlineMix_btns(
                                btns = {
                                    'Засечь': 'time2',
                                    'Подробнее': 'https://habr.com/ru/companies/click/articles/656109/'
                                }
                            )
    )
@user_private_router.message((F.text.lower() == "метод gtd"))
async def menu_command(message: types.Message):
    await message.answer("Запишите все ваши дела в блокнот или тетрадь, распределите ее по разным категориям, например 'Учеба', 'Друзья', 'Дом'. Затем, следуйте следующему"
                         " плану и постепенно выполняйте дела!",
                            reply_markup= inline.get_inlineMix_btns(
                                btns = {
                                    'Я составил список': 'Я сос',
                                    'Подробнее': 'https://habr.com/ru/articles/599391/'
                                }
                            )
    )
@user_private_router.message((F.text.lower() == "матрица эйзенхауэра"))
async def menu_command(message: types.Message):
    await message.answer("Вам нужно записать все ваши дела, распределив их на четыре группы по важности и срочности:"
                        "срочные и важные; срочные, но не важные; несрочные, но важные; несрочные и не важные",
                            reply_markup= inline.get_inlineMix_btns(
                                btns = {
                                    'Предоставь таблицу': 'табло',
                                    'Подробнее': 'https://skillbox.ru/media/management/matritsa_eyzenkhauera/'
                                }
                            )
    )
@user_private_router.callback_query(F.data.startswith("табло"))
async def process_callback_button(callback_query: types.CallbackQuery):
    try:
        file_path = 'C:\images\matrix.jpg'
        photo = types.FSInputFile(path = file_path)
        await bot.send_photo(chat_id=callback_query.message.chat.id, photo=photo)
        await bot.send_message(callback_query.message.chat.id, "Хорошо потрудиться!")
    except FileNotFoundError:
        await bot.send_message(callback_query.message.chat.id, "Изображение не найдено.")
    except Exception as e:
        await bot.send_message(callback_query.message.chat.id, f"Произошла ошибка: {e}")

@user_private_router.callback_query(F.data.startswith("Я сос"))
async def process_callback_button(callback_query: types.CallbackQuery):
    try:
        file_path = 'C:\images\GTD.jpg'
        photo = types.FSInputFile(path = file_path)
        await bot.send_photo(chat_id=callback_query.message.chat.id, photo=photo)
        await bot.send_message(callback_query.message.chat.id, "Успешной работы!")
    except FileNotFoundError:
        await bot.send_message(callback_query.message.chat.id, "Изображение не найдено.")
    except Exception as e:
        await bot.send_message(callback_query.message.chat.id, f"Произошла ошибка: {e}")

@user_private_router.callback_query(F.data.startswith("t"))
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)

    if callback_query.data == 'time1':
        await bot.edit_message_text("Время пошло! Работайте 25 минут 💻", 
                                     chat_id=str(callback_query.from_user.id), 
                                     message_id=callback_query.message.message_id)
        await asyncio.sleep(25*60)
        await bot.edit_message_text("Время вышло! Сделайте большой или маленький перерыв и возвращайтесь 🥂 ", 
                                     chat_id=str(callback_query.from_user.id), 
                                     message_id=callback_query.message.message_id)
    
    elif callback_query.data == 'time2':
        await bot.edit_message_text("Время пошло! Работайте 90 минут 💻", 
                                     chat_id=str(callback_query.from_user.id), 
                                     message_id=callback_query.message.message_id)
        await asyncio.sleep(90*60)
        await bot.edit_message_text("Время вышло! Сделайте перерыв 30 минут и возвращайтесь 🥂", 
                                     chat_id=str(callback_query.from_user.id), 
                                     message_id=callback_query.message.message_id)
#----------------------------------------------Музычка-------------------------------------------
@user_private_router.message(or_f(Command('music'), (F.text.lower() == "музыка")))
async def process_callback_button(message: types.Message):
    await message.answer("Многие любят выполнять свои обязанности под тихую музыку на фоне 🎧 она помогает работать дольше и делать это в более хорошем настроении. "
                         "Чтож, какое настроение сегодня?🤗", 
                         reply_markup= inline.get_inlineMix_btns(
                             btns = {
                                "Мрачноеִֶ 🦇" : 'мрачное',
                                "Сосредоточенное 🎯" : 'серьезное',
                                "Спокойное 😌" : 'спокойное',
                                "Боевое 🎸" : 'боевое',
                             }
                         ),
    )

@user_private_router.callback_query(F.data.startswith('бо'))
async def info_panel(callback_query: types.CallbackQuery):
    await bot.send_message(
        chat_id=callback_query.from_user.id,  
        text=("Отлично, я вижу, что вы готовы драться не на жизнь, а насмерть 🪓 Только пообещайте не отвлекаться! Хорошей работы! "),
        reply_markup=inline.get_inlineMix_btns(
            btns={
                "Зов севера": 'https://youtu.be/9WXsdApQIY4?si=DkLEiYA_Kl90wsOU',
                "Вигвам шамана": 'https://youtu.be/_Nqlg_hZdVc?si=l24THmcdVUb58M7o',
                "Мудрость дракона": 'https://youtu.be/2rcckLnrAbg?si=XNG7_pKmVYj8oCcA',
                "Тяжелый метал": 'https://my.mail.ru/mail/alex-enm/video/46908/714343.html?from=videoplayer',
            }
        )
    )
    await callback_query.answer()
    



@user_private_router.callback_query(F.data.startswith('спок'))
async def info_panel(callback_query: types.CallbackQuery):
    await bot.send_message(
        chat_id=callback_query.from_user.id,  
        text=("Рад, что вы сегодня спокойны 🌊 с вашими задачами вам поможет справиться приятный джаз и Lo-Fi, приятного прослушивания! "),
        reply_markup=inline.get_inlineMix_btns(
            btns={
                "Lo-fi": 'https://www.youtube.com/live/d2VdpHxmbPE?si=rLOMXqrqgFabNSZd',
                "Chill Lo-fi": 'https://youtu.be/CLeZyIID9Bo?si=3yI1pOfC22Zlsk2w',
                "Спокойный джаз": 'https://www.youtube.com/live/2oWN7waCXIo?si=M1q5WbXAivpAs-NH',
                "Босса нова": 'https://youtu.be/7GkHh3qLwgU?si=7HhQRYjk0CskJA0U',
            }
        )
    )
    await callback_query.answer()
    


@user_private_router.callback_query(F.data.startswith('серь'))
async def info_panel(callback_query: types.CallbackQuery):
    await bot.send_message(
        chat_id=callback_query.from_user.id,  
        text=("Вижу вы настроены на продуктивную работу! 🖥️ Готов поспорить, с этой музыкой ваше задание "
              "выполнится проще"),
        reply_markup=inline.get_inlineMix_btns(
            btns={
                "Глубокая концентрация": 'https://youtu.be/j8L6IvuYGOQ?si=hGsxDzCnWRp1jjWM',
                "Ночной город": 'https://youtu.be/n9Y2Eb4BaSg?si=IXw-eY6Wrlx41JPg',
                "Осенний вечер": 'https://youtu.be/m6SOJlkN1zU?si=zPwF_mCPxXOeuMK2',
                "Научная музыка": 'https://youtu.be/5i0Z0E5yaYI?si=Ys6Bm3yzDPCercDp',
            }
        )
    )
    await callback_query.answer()
    

@user_private_router.callback_query(F.data.startswith('мрач'))
async def info_panel(callback_query: types.CallbackQuery):
    await bot.send_message(
        chat_id=callback_query.from_user.id,  
        text=("С таким настроением только строить великие планы и совершать великие деяния!⚔️ "
              "Вот несколько вариантов для продуктивной работы, но не забывайте, "
              "что даже великие не забывали отдыхать и совершали ошибки 🛡️"),
        reply_markup=inline.get_inlineMix_btns(
            btns={
                "Гром и классика": 'https://youtu.be/86WzoZt-ezs?si=fBGxVPG1ARWeptER',
                "Величие Рима": 'https://youtu.be/hC0Th-HZx5M?si=g_NkzZA58RRQmy2X',
                "Стойкость и терпение": 'https://youtu.be/Mbb_un0rkH4?si=ooE2r5hLnQhVIuyd',
                "Пугающее средневековье": 'https://youtu.be/-ZWwmVDQ20Q?si=4cpfWbpLq44HNY3N',
            }
        )
    )
    await callback_query.answer()















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