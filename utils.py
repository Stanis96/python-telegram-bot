from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def validate_age():
    inlinekeyboard = [
        [
            InlineKeyboardButton("Да", callback_data="Да"),
            InlineKeyboardButton("Нет", callback_data="Нет"),
        ]
    ]
    return InlineKeyboardMarkup(inlinekeyboard)


def get_menu_buttons():
    buttons = [
        ["Бары и филиалы"],
        [
            KeyboardButton("Поиск напитка"),
        ],
        [KeyboardButton("Бары рядом со мной", request_location=True)],
    ]
    return ReplyKeyboardMarkup(one_time_keyboard=True, keyboard=buttons)
