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
    await message.answer(f'Привет {message.from_user.first_name}.'+
                         '\nЭтот бот поможет узнать баллы и посещяемость студента на определенных дисциплинах'+
                         '\nВыберите дисциплину:', reply_markup = select_subject )
    await state.set_state(Send.sub)


async def Page(message: Message, bot: Bot, state: FSMContext):
    df_orders = pd.read_excel(f'DB.xls', sheet_name='OPD', skiprows=0)
    nameme =  message.text

    row = df_orders[df_orders.isin([nameme]).any(axis=1)]
    id_user = (row.to_string().split())[3]
    print(nameme, "\n", row)
    await state.update_data(name=id_user)

    if nameme in df_orders.values:
        await message.answer(f'Какие данные {nameme} вы хотите узнать? ', reply_markup=select_page)
        await state.set_state(Send.page)
    else:
        await message.answer('Проверьте правильность ввода, и введите заново')








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
