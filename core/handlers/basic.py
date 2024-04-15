import pandas as pd
from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
# from core.keyboards.reply import keyboard
import time
from core.keyboards.inline import select_subject, select_page
from core.utils.states import Send

admin = 1024576085


async def get_start(message: Message, bot: Bot, state: FSMContext):
    await message.answer(f'Привет {message.from_user.first_name}.\nЭтот бот поможет узнать баллы и посещяемость студента на определенных дисциплинах \nВыберите дисциплину:', reply_markup = select_subject )
    await state.set_state(Send.sub)





async def Page(message: Message, bot: Bot, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(f'Какие данные {message.text} вы хотите узнать? ')
    await message.answer('Что хотите узнать?', reply_markup=select_page)
    await state.set_state(Send.page)





async def db_read(call: CallbackQuery, bot: Bot):
    page = call.data.split('_')[1]
    df_orders = pd.read_excel(f'DB.xls', sheet_name = 'OPD', skiprows=0)
    if page == 'visit':
        await call.message.answer(f'{df_orders.iloc[4, 2]}%')
        print(f'{df_orders.iloc[4, 2]}%')
    else:
        await call.message.answer(f'{df_orders.iloc[4,1]} балл')
        print(f'баллы по предмету: {df_orders.iloc[4,1]} ')
    await call.answer()

async def send_photo(message: Message, bot: Bot, state: FSMContext):
    await message.answer(f'Скинь мне фото пожалуйста!')
    await state.set_state(Send.photo)


async def get_photo(message: Message, bot: Bot, state: FSMContext):
    await message.answer(f'Отлично. Теперь твоя фотка в моих сохраненках _-_')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.send_message(admin, text='фоточки подъехали')
    await bot.download_file(file.file_path, 'fileSave/photo{}.jpg'.format(time.time()))
    await state.update_data(photo = 'photo{}.jpg'.format(time.time()))
    await state.clear()
