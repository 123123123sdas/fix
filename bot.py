from aiogram import Bot, Dispatcher, executor, types
import logging, os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("Привет! Я бот-продавец крипто-прогнозов 💰")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
