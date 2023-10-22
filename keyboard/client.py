from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton

buy_button = KeyboardButton(text='список ботов')
categories_button = KeyboardButton(text='выбрать категорию')
search_button = KeyboardButton(text='поиск по названию/описанию')


keyboard_client = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[[buy_button, ], [categories_button, ], [search_button, ]]
)
