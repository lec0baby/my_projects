from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from state.register import RegisterState
import re
import os
from utils.database import Database


async def start_register(message: Message, state: FSMContext):
    db = Database(os.getenv('DATABASE_NAME'))
    users = db.select_user_id(message.from_user.id)
    if(users):
        await message.answer(f'{users[1]}, Вы уже зарегистрированы!')
    else:
        await message.answer(f'Давайте начнём регистрацию \nДля начала скажите как к Вам обращаться?')
        await state.set_state(RegisterState.regName)


async def register_name(message: Message, state: FSMContext):
    await message.answer(f'Приятно познакомиться, {message.text} \n'
                         f'Теперь укажите номер телефона, чтобы быть на связи \n'
                         f'Формат телефона: +7********** \n\n'
                         f'Внимание! Я чувствителен к формату')
    await state.update_data(regname=message.text)
    await state.set_state(RegisterState.regPhone)

async def register_phone(message: Message, state: FSMContext):
    if(re.findall('^\+?[7][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$', message.text)):
        await state.update_data(regphone=message.text)
        reg_data = await state.get_data()
        reg_name = reg_data.get('regname')
        reg_phone = reg_data.get('regphone')
        msg = f'Приятно познакомиться, {reg_name} \n\n Телефон - {reg_phone}'
        await message.answer(msg)
        db = Database(os.getenv('DATABASE_NAME'))
        db.add_user(reg_name, reg_phone, message.from_user.id)
        await state.clear()
    else:
        await message.answer(f'Номер указан в неправильном формате')