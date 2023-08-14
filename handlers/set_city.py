import sqlite3

from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext
from handlers.user import User_Dates
from keyboards import main_keyboard

conn = sqlite3.connect('db/Weather_bot.db', check_same_thread=False)
cursor = conn.cursor()


async def city_ask(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Напиши интересующий тебя город!')
    await state.set_state(User_Dates.waiting_city.state)


async def city_answer(message: types.Message, state: FSMContext):
    city = str(message.text.lower()).capitalize()
    keyboard = main_keyboard.main_keyboard_def()
    user_id = message.from_user.username
    cursor.execute(f"""UPDATE users SET city='{city}' WHERE id='{user_id}' """)
    conn.commit()
    await message.answer(f'Хорошо, так и запишем, {city}.',
                         reply_markup=keyboard)
    await state.finish()


def register_handlers_set_city(dp: Dispatcher):
    dp.register_callback_query_handler(city_ask, lambda call: call.data == 'city_input')
    dp.register_message_handler(city_answer, state=User_Dates.waiting_city)
