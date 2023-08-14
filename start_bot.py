from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token='YOUR_BOT_TOKEN')
weather_api = "YOUR_API_KEY"

dp = Dispatcher(bot, storage=MemoryStorage())
