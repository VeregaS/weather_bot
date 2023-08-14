import sqlite3
import requests

from start_bot import weather_api
from aiogram import types
from aiogram.dispatcher import Dispatcher

conn = sqlite3.connect('db/Weather_bot.db', check_same_thread=False)
cursor = conn.cursor()

api_key = weather_api

icons = ['☀️', '🌤️', '☁️', '🌧️', '🌦️', '⛈️', '❄️', '🌫️️']

thunderstorm_group = ['thunderstorm with light rain', 'thunderstorm with rain',
                      'thunderstorm with heavy rain', 'light thunderstorm',
                      'thunderstorm', 'heavy thunderstorm',
                      'ragged thunderstorm', 'thunderstorm with light drizzle',
                      'thunderstorm with drizzle', 'thunderstorm with heavy drizzle']
# 5

drizzle_group = ['light intensity drizzle', 'drizzle',
                 'heavy intensity drizzle', 'light intensity drizzle rain',
                 'drizzle rain', 'heavy intensity drizzle rain',
                 'shower rain and drizzle', 'heavy shower rain and drizzle',
                 'shower drizzle', 'light intensity shower rain', 'shower rain',
                 'heavy intensity shower rain', 'ragged shower rain']
# 3

rain_group_1 = ['light rain', 'moderate rain', 'heavy intensity rain', 'very heavy rain',
                'extreme rain']
# 4

snow_group = ['light snow', 'snow', 'heavy snow', 'sleet', 'light shower sleet',
              'shower sleet', 'light rain and snow', 'rain and snow',
              'light shower snow', 'shower snow', 'heavy shower snow',
              'freezing rain']
# 6

atmosphere_group = ['mist', 'smoke', 'haze', 'sand/dust whirls', 'fog', 'sand',
                    'dust', 'volcanic ash', 'squalls', 'tornado']
# 7

clear_group = ['clear sky']
# 0

clouds_group_1 = ['few clouds: 11-25%']
# 1

clouds_group_2 = ['scattered clouds', 'broken clouds',
                  'overcast clouds']


# 2

async def main_function(call: types.CallbackQuery):
    try:
        user_id = call.from_user.username
        data = [str(i) for i in cursor.execute(f"SELECT city FROM users WHERE id='{user_id}'").fetchall()]
        city = data[0].replace('(\'', '').replace("\',)", "")
        text = get_weather(city, api_key)
        await call.message.answer(f'{text}')
    except Exception as ex:
        await call.message.answer("Укажите город!")


def get_weather(city, api_key):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&lang=eng&appid={api_key}&units=metric")
        output = r.json()
        city_name = output['name']
        feels_like_temp = output['main']['feels_like']
        wind_speed = output['wind']['speed']
        description = output['weather'][0]['description']
        weather = "Погода не определена."
        if description in clear_group:
            weather = icons[0]
        if description in clouds_group_1:
            weather = icons[1]
        if description in clouds_group_2:
            weather = icons[2]
        if description in drizzle_group:
            weather = icons[3]
        if description in rain_group_1:
            weather = icons[4]
        if description in thunderstorm_group:
            weather = icons[5]
        if description in snow_group:
            weather = icons[6]
        if description in atmosphere_group:
            weather = icons[7]
        text = f"🏙ㅤ{city_name}\n\n" \
               f"{weather}ㅤ—ㅤза окном\n" \
               f"🌡ㅤ—ㅤ{'%.0f' % feels_like_temp}°\n" \
               f"💨ㅤ—ㅤ{'%.1f' % wind_speed} м/с\n"
        return text
    except Exception as ex:
        return "Ошибка! Попробуйте позже"


def register_handlers_main_function(dp: Dispatcher):
    dp.register_callback_query_handler(main_function, lambda call: call.data == 'weather_report')
