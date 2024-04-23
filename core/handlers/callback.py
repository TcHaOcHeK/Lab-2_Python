import pandas as pd

from aiogram import Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from core.utils.states import Send



async def select_subject( call: CallbackQuery, bot: Bot, state: FSMContext):
    sub = call.data.split('_')[1]
    await call.message.answer(f'вы выбрали {sub}')
    await state.update_data(sub=sub)
    await call.message.answer('Введите имя и фамилию студента, чьи данные вы хотите увидеть.')
    await state.set_state(Send.name)
    await call.answer()


async def select_page(call: CallbackQuery, bot: Bot, state: FSMContext):
    page = int(call.data.split('_')[1])
    await state.update_data(page=page)
    data = await state.get_data()
    df_orders = pd.read_excel(f'DB.xlsx', sheet_name = data.get('sub'), skiprows=0)
    await call.message.answer(f'{df_orders.iloc[int(data.get('name')), data.get('page')]}')
        # print(f'{df_orders.iloc[int(data.get('name')), 2]}%')


    await call.answer()







