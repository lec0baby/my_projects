from aiogram import Bot, Dispatcher, F
import asyncio
from dotenv import load_dotenv
import os
from aiogram.filters import Command

from utils.commands import set_commands
from handlers.start import get_start
from state.register import RegisterState
from state.create import CreateState
from handlers.register import start_register, register_name, register_phone
from filters.CheckAdmin import CheckAdmin
from handlers.admin.create import create_game, select_place, select_date, select_time, select_minplayer, select_maxplayer, select_price


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
dp.callback_query.register(select_place, CreateState.place)
dp.callback_query.register(select_date, CreateState.date)
dp.callback_query.register(select_time, CreateState.time)
dp.callback_query.register(select_minplayer, CreateState.minplayer)
dp.callback_query.register(select_maxplayer, CreateState.maxplayer)
dp.callback_query.register(select_price, CreateState.price)

async def start():
    await set_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())