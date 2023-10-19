from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardBuilder


buy_button = KeyboardButton(text='/список_ботов')
categories_button = KeyboardButton(text='/выбрать_категорию')


keyboard_client = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[buy_button, ], [categories_button, ]])



