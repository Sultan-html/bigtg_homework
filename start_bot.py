import asyncio
import logging
from aiogram import Bot, Dispatcher
from handler import router


bot = Bot(token='7063883108:AAGKBYigdI1KzJSTob2TGj1APtWY2EclfDA')
dp = Dispatcher(bot=bot)

async def main():
    dp.include_router(router)  
    await dp.start_polling(bot) 
try:
    if __name__ == "__main__":
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())  
except KeyboardInterrupt:
    print("exit")