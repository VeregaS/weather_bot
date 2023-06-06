from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token='6284815295:AAHk1SKNRExV7d0x49D32uu2RfWjZAmr2Zo')
dp = Dispatcher(bot, storage=MemoryStorage())
