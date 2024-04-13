from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

reply_keyboard = ReplyKeyboardMarkup(keyboard = [
    [
        KeyboardButton(
            text = 'Ряд 1. пенис'
        ),
        KeyboardButton(
            text = 'Ряд 1. Кнопка 2'
        ),
        KeyboardButton(
            text = 'Ряд 1. Кнопка 3'
        ),
    ],
    [
        KeyboardButton(
            text = 'Ряд 2. Кнопка 1'
        ),
        KeyboardButton(
            text = 'Ряд 2. Кнопка 2'
        ),
        KeyboardButton(
            text = 'Ряд 2. Кнопка 3'
        ),
    ]
], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выбери кнопку', selective=True)