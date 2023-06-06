from aiogram.utils import executor
from start_bot import dp
from handlers import user, set_city, weather_forecast


user.register_handlers_user(dp)
set_city.register_handlers_set_city(dp)
weather_forecast.register_handlers_main_function(dp)


if __name__ == '__main__':
    executor.start_polling(dp)
