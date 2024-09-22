from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Меню"),
            KeyboardButton(text="Техники"),
            KeyboardButton(text="Музыка"),
            KeyboardButton(text="Поддержать дух"),
        ],
    ], 
    resize_keyboard= True

)
