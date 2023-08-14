from aiogram import types


def main_keyboard_def():
    keyboard_main = types.InlineKeyboardMarkup()
    keyboard_main.add(types.InlineKeyboardButton(text="⛅️ㅤПрогноз погодыㅤ⛅️", callback_data="weather_report"))
    keyboard_main.add(types.InlineKeyboardButton(text="👤ㅤ Профиль ㅤ👤", callback_data="profile"))
    return keyboard_main
