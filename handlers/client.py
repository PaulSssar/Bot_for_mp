import requests
from config import URL
from aiogram import F, Router
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from keyboard.client import keyboard_client, categories_kb

router = Router()


@router.message(F.text == '/start')
async def command_start(message: types.Message):
    await message.answer("""Здравствуйте! Я бот маркетплейса телеграм ботов для транспорта.
        Чем могу Вам помочь?""", reply_markup=keyboard_client)


@router.message(F.text == '/список_ботов')
async def list_bots(message: types.Message):
    bots = requests.get(URL + 'bots').json()
    bot_list = bots['results']
    for bot in bot_list:
        await message.answer_photo(photo=types.URLInputFile(bot['main_photo']))
        await message.answer(f"{bot['name']}\n{bot['description']}\n Цена: {bot['price']}",
                             reply_markup=InlineKeyboardMarkup(
                                 inline_keyboard=[
                                     [InlineKeyboardButton(
                                         text='Купить',
                                         url=URL + 'bots/' + str(bot['id']))]
                                 ]))


@router.message(F.text == '/выбрать_категорию')
async def categories(message: types.Message):
    await message.answer(text='Выберите категорию',
                         reply_markup=categories_kb())
