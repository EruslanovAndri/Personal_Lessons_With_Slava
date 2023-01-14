from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

command_defoult_keyboard = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text='/Start'),
            KeyboardButton(text='/Help')

        ],
        [
            KeyboardButton(text='/Item')
        ],
        [
            KeyboardButton(text='Подтвердить номер телефона',request_contact=True)
        ],
        [
            KeyboardButton(text='/Buy')
        ]
    ],
    resize_keyboard=True

)