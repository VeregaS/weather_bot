from aiogram import types


def profile_to_main_def():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="🏠ㅤ Указать город ㅤ🏠", callback_data="city_input"))
    keyboard.add(types.InlineKeyboardButton(text="◀️ㅤНазадㅤ◀️", callback_data="back"))
    return keyboard
