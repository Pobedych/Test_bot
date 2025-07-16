from logging import config
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

bot = Bot(token=config('TOKEN'))
dp = Dispatcher(storage=MemoryStorage())    

