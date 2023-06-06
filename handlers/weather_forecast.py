import sqlite3
import requests
from pprint import pprint
from aiogram import types
from aiogram.dispatcher import Dispatcher

conn = sqlite3.connect('db/Weather_bot.db', check_same_thread=False)
cursor = conn.cursor()

api_key = "bdc4604cb4b508c43185f6261a0f66e4"


async def main_function(call: types.CallbackQuery):
    try:
        user_id = call.from_user.username
        data = [str(i) for i in cursor.execute(f"SELECT city FROM users WHERE id='{user_id}'").fetchall()]
        print(data)
        city = data[0].replace('(\'', '').replace("\',)", "")
        text = get_weather(city, api_key)
        await call.message.answer(f'{text}')
    except Exception as ex:
        await call.message.answer("Укажите город!")


def get_weather(city, api_key):
    try:
        r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&appid={api_key}&units=metric")
        output = r.json()
        pprint(output)
        city_name = output['name']
        feels_like_temp = output['main']['feels_like']
        wind_speed = output['wind']['speed']
        description = output['weather'][0]['description']
        text = f"🏙ㅤ{city_name}ㅤ🏙\n" \
               f"{description.capitalize()}\n" \
               f"Ощущается как {'%.0f' % feels_like_temp}°\n" \
               f"Ветер {wind_speed} м/с\n" \
               f"Хорошего дня!"

        return text
    except Exception as ex:
        return "Ошибка! Попробуйте позже"


def register_handlers_main_function(dp: Dispatcher):
    dp.register_callback_query_handler(main_function, lambda call: call.data == 'weather_report')
