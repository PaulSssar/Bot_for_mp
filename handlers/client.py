import requests
from aiogram import F, Router
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import keyboard.client

router = Router()


@router.message(F.text == '/start')
async def command_start(message: types.Message):
    await message.answer("""Здравствуйте! Я бот маркетплейса телеграм ботов для транспорта.
        Чем могу Вам помочь?""", reply_markup=keyboard.client.keyboard_client)


@router.message(F.text == '/список_ботов')
async def list_bots(message: types.Message):
    bots = requests.get('http://80.87.96.7/api/bots/').json()
    bot_list = bots['results']
    for bot in bot_list:
        await message.answer_photo(photo=types.URLInputFile(bot['main_photo']))
        await message.answer(f"{bot['name']}\n{bot['description']}\n Цена: {bot['price']}",
                             reply_markup=InlineKeyboardMarkup(
                                 inline_keyboard=[
                                     [InlineKeyboardButton(
                                         text='Купить',
                                         url='http://80.87.96.7/api/bots/' + str(bot['id']))]
                                 ]))


@router.message(F.text == '/выбрать_категорию')
async def categories(message : types.Message):
    categories = requests.get('http://80.87.96.7/api/categories/').json()
    buttons = [[KeyboardButton(text=category['name'])] for category in categories]
    categories_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=buttons)
    await message.answer(text='Выберите категорию',
                         reply_markup=categories_kb)




