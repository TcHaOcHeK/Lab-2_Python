from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

select_subject = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='ОПД',
            callback_data = 'subject_OPD'
        )
    ],
    [
        InlineKeyboardButton(
            text='Программирование',
            callback_data = 'subject_Prog'
        )
    ],
    [
        InlineKeyboardButton(
            text='ПРД',
            callback_data = 'subject_PRD'
        )
    ]

], resize_keyboard = True, one_time_keyboard=True)


select_page = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Баллы',
            callback_data = 'page_grate'
        ),
        InlineKeyboardButton(
            text='Посещаемость',
            callback_data = 'page_visit'
        )
    ]

], resize_keyboard = True, one_time_keyboard=True)