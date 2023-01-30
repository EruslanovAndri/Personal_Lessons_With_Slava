from aiogram.utils import executor
from handlers_paket import dp

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)

