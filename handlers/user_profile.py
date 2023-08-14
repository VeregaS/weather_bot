import sqlite3
from aiogram import types
from aiogram.dispatcher import Dispatcher
from keyboards import profile_to_main, main_keyboard

conn = sqlite3.connect('db/Weather_bot.db', check_same_thread=False)
cursor = conn.cursor()


async def profile_main_page(call: types.CallbackQuery):
    keyboard = profile_to_main.profile_to_main_def()
    user_id = call.from_user.username
    user_name = call.from_user.id
    data = cursor.execute(f"SELECT id, city, name FROM users WHERE id='{user_id}'").fetchall()[0]
    print(data)
    tg = data[0]
    city = data[1]
    name = data[2]
    await call.message.edit_text(f'ID: {user_name}\n'
                                 f'Tg: @{tg}\n'
                                 f'Город: {city}', reply_markup=keyboard)


async def back_to_main_page_fake(call: types.CallbackQuery):
    keyboard = main_keyboard.main_keyboard_def()
    user_name = call.from_user.username
    user_id = call.from_user.username
    await call.message.edit_text(f"Привет, @{user_name}!\n", reply_markup=keyboard)


def register_handlers_user_profile(dp: Dispatcher):
    dp.register_callback_query_handler(profile_main_page, lambda call: call.data == 'profile')
    dp.register_callback_query_handler(back_to_main_page_fake, lambda call: call.data == 'back')
