import pandas as pd
import pygsheets
from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
# from core.keyboards.reply import keyboard
import time
from core.keyboards.inline import select_subject, select_page
from core.utils.states import Send

admin = 1024576085
client = pygsheets.authorize(service_file='../TG-Bot_lab2_Python/pybot-420905-dfb4d55e741a.json')


def dbLoad():
    sheet = client.open('Botik_Sheets')
    worksheets = sheet.worksheets()

    # Создание нового экземпляра ExcelWriter для записи в файл Excel
    with pd.ExcelWriter('DB.xlsx', engine='xlsxwriter') as writer:
        for worksheet in worksheets:
            data = worksheet.get_as_df()
            # Запись каждого листа в отдельный лист в файле Excel
            data.to_excel(writer, sheet_name=worksheet.title, index=False)

    # Сообщение об успешном завершении процесса
    print("Данные успешно скопированы в файл Excel")


async def get_start(message: Message, bot: Bot, state: FSMContext):
    await message.answer(f'Привет {message.from_user.first_name}.'+
                         '\nЭтот бот поможет узнать баллы и посещяемость студента на определенных дисциплинах'+
                         '\nВыберите дисциплину:', reply_markup = select_subject )
    await state.set_state(Send.sub)
    dbLoad()


async def Page(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    df_orders = pd.read_excel(f'DB.xlsx', sheet_name=f'{data.get('sub')}', skiprows=0)

    nameme = message.text.lower()

    row = df_orders[df_orders.isin([nameme]).any(axis=1)]
    id_user = (row.to_string().split())[3]
    print(nameme, "\n", row)


    if nameme in df_orders.values:
        await message.answer(f'Какие данные {nameme} вы хотите узнать? ', reply_markup=select_page)
        await state.set_state(Send.page)
        await state.update_data(name=id_user)
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
