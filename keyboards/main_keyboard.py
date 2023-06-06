from aiogram import types


def main_keyboard_def():
    keyboard_main = types.InlineKeyboardMarkup()
    keyboard_main.add(types.InlineKeyboardButton(text="Узнать прогноз погоды", callback_data="weather_report"))
    keyboard_main.add(types.InlineKeyboardButton(text="Указать город", callback_data="city_input"))
    return keyboard_main
