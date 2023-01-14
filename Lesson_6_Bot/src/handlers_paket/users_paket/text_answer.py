from loader import *

@dp.message_handler(text=['Начать','Привет'])  # тут реакция не на команду, а на текс!!!
async def answer_start_command(message: types.Message):  # функция ответа на команду в боте
    await message.answer(text=f'Hello!'f'\n Glad to hear you!')