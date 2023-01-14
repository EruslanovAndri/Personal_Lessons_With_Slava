import sqlite3
from pathlib import Path
from aiogram import Bot, Dispatcher, types
from config import TOKEN
from db_api_paket import Database

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db_path = Path('db_api_paket', 'database', 'shop_database.db')
db = Database(db_path=db_path)
try:
    db.create_tabel_users()
except sqlite3.OperationalError as e:
    print(e)
except Exception as e:
    print(e)

try:
    db.create_tabel_items()
except sqlite3.OperationalError as e:
    print(e)
except Exception as e:
    print(e)

