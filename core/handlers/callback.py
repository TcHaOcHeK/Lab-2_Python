import pandas as pd
from aiogram import Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from core.utils.states import Send

state = ' '


async def select_subject( call: CallbackQuery, bot: Bot, state: FSMContext):
    sub = call.data.split('_')[1]
    await call.message.answer(f'вы выбрали {sub}')
    await state.update_data(sub=sub)
    await call.message.answer('Введите имя и фамилию студента, чьи данные вы хотите увидеть.')
    await state.set_state(Send.name)
    await call.answer()


async def select_page(call: CallbackQuery, bot: Bot, state: FSMContext):
    page = call.data.split('_')[1]
    if page == 'visit':
        page = 2
    else:
        page = 1
    print('yep')
    await state.update_data(page=page)
    await state.clear()
    await call.answer()






