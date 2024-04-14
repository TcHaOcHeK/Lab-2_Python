from aiogram import Bot
from aiogram.types import CallbackQuery
import pandas as pd
state = ' '


async def select_subject(call: CallbackQuery, bot: Bot):

    sub = call.data.split('_')[1]
    answer = f'вы выбрали {sub}'

    await call.message.answer(answer)
    await call.answer()


async def select_page(call: CallbackQuery, bot: Bot):

    sub = call.data.split('_')[1]
    answer = f'вы выбрали {sub}'

    await call.message.answer(answer)
    await call.answer()


async def db_read(call: CallbackQuery, bot: Bot):
    sub = call.data.split('_')[1]
    state = sub
    df_orders = pd.read_excel(f'DB.xls', sheet_name = f'{sub}')
    print(df_orders)
    await call.answer()


async def db_read_only_grate(call: CallbackQuery, bot: Bot):
    page = call.data.split('_')[1]
    df_orders = pd.read_excel(f'DB.xls', sheet_name = 'OPD', skiprows=0)
    if page == 'visit':
        await call.message.answer(f'{df_orders.iloc[4, 2]}%')
        print(f'{df_orders.iloc[4, 2]}%')
    else:
        await call.message.answer(f'{df_orders.iloc[4,1]} балл')
        print(f'баллы по предмету: {df_orders.iloc[4,1]} ')
    await call.answer()


