import requests
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardBuilder
from config import URL

buy_button = KeyboardButton(text='/список_ботов')
categories_button = KeyboardButton(text='/выбрать_категорию')

keyboard_client = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[buy_button, ], [categories_button, ]])


def categories_kb():
    categories = requests.get(URL + 'categories/').json()
    buttons = [[KeyboardButton(text=category['name'])] for category in categories]
    categories_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=buttons)
    return categories_kb

