import asyncio
import logging


from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import handlers
import config


async def main():
    bot = Bot(token=config.TOKEN, parse_mode=ParseMode.HTML)
    memory = MemoryStorage()
    dp = Dispatcher(memory=memory)
    dp.include_router(handlers.client.router)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())



