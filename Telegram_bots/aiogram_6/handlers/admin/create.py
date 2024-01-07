from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from Telegram_bots.aiogram_6.keyboards.create_kb import place_kb, date_kb, time_kb
from Telegram_bots.aiogram_6.state.create import CreateState


async def create_game(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id, f'Выберите площадку, где будет проходить игра', reply_markup=place_kb())
    await state.set_state(CreateState.place)


async def select_place(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Место игры выбрано! \n'
                              f'Дальше выберите дату', reply_markup=date_kb())
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.set_state(CreateState.date)


async def select_date(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Дата игры успешно сохранена \n'
                              f'Выберите время игры', reply_markup=time_kb())
    await state.update_data(date=call.data)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.set_state(CreateState.time)


async def select_time(call: CallbackQuery, state: FSMContext):
    await call.message.answer(f'Укажите минимальное количество игроков от 4 до 16')
    await state.update_data(time=call.data)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.set_state(CreateState.minplayer)


async def select_minplayer(message: Message, state: FSMContext, bot: Bot):
    if(message.text.isdigit() and 4 <= int(message.text) <= 16):
        await bot.send_message(message.from_user.id, f'Хорошо, теперь укажите максимальное количество игроков от 4 до 16')
        await state.update_data(minplayer=message.text)
        await state.set_state(CreateState.maxplayer)
    else:
        await bot.send_message(message.from_user.id, f'Я жду число от 4 до 16')


async def select_maxplayer(message: Message, state: FSMContext, bot: Bot):
    if(message.text.isdigit() and 4 <= int(message.text) <= 16):
        await bot.send_message(message.from_user.id, f'Теперь укажите стоимость игры')
        await state.update_data(maxplayer=message.text)
        await state.set_state(CreateState.price)
    else:
        await bot.send_message(message.from_user.id, f'Я жду число от 4 до 16')


async def select_price(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id, f'Отлично, я записал игру')
    await state.update_data(price=message.text)
    create_data = await state.get_data()
    print(create_data)
