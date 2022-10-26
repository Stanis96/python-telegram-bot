import requests

from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from settings import URL_API


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


def get_query(tag):
    try:
        result = requests.get(URL_API + tag)
        return result.json()
    except (requests.RequestException, ValueError):
        print("Error")
        return False
