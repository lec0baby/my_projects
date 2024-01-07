from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from Telegram_bots.aiogram_6.keyboards.create_kb import place_kb
from Telegram_bots.aiogram_6.state.create import CreateState


async def create_game(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id, f'Выберите площадку, где будет проходить игра', reply_markup=place_kb())
    await state.set_state(CreateState.place)

async def select_place(call: CallbackQuery, state: FSMContext, bot: Bot):
    await call.message.answer(f'Место игры выбрано! \n'
                              f'Дальше выберите дату')
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer()
    await state.set_state(CreateState.data)
