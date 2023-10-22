import requests
from config import URL
from aiogram import F, Router
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardBuilder
from keyboard.client import keyboard_client

router = Router()


@router.message(F.text == '/start')
async def command_start(message: types.Message):
    await message.answer("""Здравствуйте! Я бот маркетплейса телеграм ботов для транспорта.
        Чем могу Вам помочь?""", reply_markup=keyboard_client)


@router.message(F.text == 'список ботов')
async def list_bots(message: types.Message, url=URL + 'bots/?limit=4'):
    bots = requests.get(url).json()
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
    buttons = []
    if bots['next']:
        buttons.append(InlineKeyboardButton(text='Вперед', callback_data=bots['next']))
    if bots['previous']:
        buttons.append(InlineKeyboardButton(text='Назад', callback_data=bots['previous']))
    if bots['next'] or bots['previous']:
        await message.answer(
            'Можете просмотреть еще несколько ботов или вернуться назад.',
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[buttons]
            )
        )


@router.message(F.text == 'выбрать категорию')
async def categories(message: types.Message):
    categories = requests.get(URL + 'categories/').json()
    buttons = InlineKeyboardBuilder()
    for category in categories:
        buttons.button(
            text=category['name'],
            callback_data=URL + 'bots/?categories=' + str(category['id'])).adjust(2)
    await message.answer(text='Выберите категорию',
                         reply_markup=buttons.as_markup())


@router.callback_query(lambda query: query.data.startswith(URL))
async def handle_pagination(query: types.CallbackQuery):
    url = query.message.reply_markup.inline_keyboard[0][0].callback_data
    await list_bots(query.message, url)
