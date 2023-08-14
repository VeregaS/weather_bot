import sqlite3

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import main_keyboard

conn = sqlite3.connect('db/Weather_bot.db', check_same_thread=False)
cursor = conn.cursor()


class User_Dates(StatesGroup):
    waiting_city = State()


async def start(message: types.Message):
    id = [str(i) for i in cursor.execute("SELECT id FROM users").fetchall()]
    user_id = message.from_user.username
    user_name = message.from_user.id
    user_id_check = f'(\'{user_id}\',)'
    if user_id_check not in id:
        cursor.execute('INSERT INTO users (id, name) VALUES (?, ?)',
                       (user_id, user_name))
        conn.commit()
    keyboard = main_keyboard.main_keyboard_def()
    await message.answer(f"Привет, @{user_id}!\n",
                         reply_markup=keyboard)


async def help(message: types.Message):
    await message.answer("· Для того чтобы поменять город, перейдите в \"Профиль\" и нажмите на \"Указать город\"!\n\n"
                         "· После этого, когда у Вас выбран город, Вы можете узнать погоду в нём, нажав на кнопку "
                         "\"Прогноз погоды\"!")


def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
