from aiogram import Bot, Dispatcher, F
import asyncio
from dotenv import load_dotenv
import os
from aiogram.filters import Command

from utils.commands import set_commands
from handlers.start import get_start
from state.register import RegisterState
from handlers.register import start_register, register_name, register_phone
from filters.CheckAdmin import CheckAdmin
from handlers.admin.create import create_game


load_dotenv()

token = os.environ.get('TOKEN')
admin_id = os.environ.get('ADMIN_ID')

bot = Bot(token=token, parse_mode='HTML')
dp = Dispatcher()

async def start_bot(bot: Bot):
    await bot.send_message(413260909, text='Бот запущен!')


dp.startup.register(start_bot)
dp.message.register(get_start, Command(commands='start'))

# Регистрируем хендлеры регистрации
dp.message.register(start_register, F.text=='Зарегистрироваться на сайте')
dp.message.register(register_name, RegisterState.regName)
dp.message.register(register_phone, RegisterState.regPhone)
# Регистрируем хендлеры с созданием игры
dp.message.register(create_game, Command(commands='create'), CheckAdmin())

async def start():
    await set_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())