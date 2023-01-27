from loader import dp, db, bot
from loader import types
from keyboards_paket import command_defoult_keyboard, get_item_inline_keyboard, navigation_items_callback
from aiogram.types import InputFile, InputMediaPhoto


@dp.message_handler(commands='Start')  # задает команду в боте
# функция ответа на команду в боте
async def answer_start_command(message: types.Message):
    await message.answer(text=f'Hello!'f'\n Glad to hear you!',
                         reply_markup=command_defoult_keyboard)


@dp.message_handler(commands=['Help'])
async def ansewr_help_command(message: types.Message):
    await message.answer(text=f'Вы можете использовать команды:'
                         '\n /Start - Приветствие.'
                         '\n /Help - Вывод всех доступных команд.'
                         '\n /Item - Вывод всех продуктов.'
                         )


@dp.message_handler(commands=['Item'])
async def answer_item_command(message: types.Message):
    await message.answer(text='В наличии есть:'
                         '\n Часы'
                         '\n Ювелирные украшения'
                         '\n Аксессуары')


@dp.message_handler(commands=['Buy'])
async def answer_buy_command(message: types.Message):
    await message.answer(text='Товар для мужчин или для женщин?')
    # data = db.select_all_users()
    # await message.answer(data)


@dp.message_handler(content_types=['contact'])
async def answer_buy_command(message: types.Message):
    if message.contact.user_id == message.from_user.id:
        await message.answer(text='Регистрация прошла успешна.')
        db.add_user(int(message.from_user.id),
                    str(message.contact.phone_number))
    else:
        await message.answer(text='Увы!')


@dp.message_handler(text=['Список товара'])
@dp.message_handler(text=['Item'])
async def answer_menu_command(message: types.Message):
    first_item_info = db.select_item_info(id=1)
    first_item_info = first_item_info[0]
    _, description, path_to_photo, count = first_item_info
    item_text = f'Model: {description}'\
                f'\n Amount: {count}'
    photo = InputFile(path_or_bytesio=path_to_photo)
    await message.answer_photo(photo=photo,
                               caption=item_text,
                               reply_markup=get_item_inline_keyboard())


@dp.callback_query_handler(navigation_items_callback.filter(for_data='items'))
async def see_new_item(call: types.CallbackQuery):
    print(call.data)
    current_item_id = int(call.data.split(':')[-1])
    first_item_info = db.select_item_info(id=current_item_id)
    first_item_info = first_item_info[0]
    _, description, path_to_photo, count = first_item_info
    item_text = f'Model: {description}'\
                f'\n Amount: {count}'

    photo = InputFile(path_or_bytesio=path_to_photo)
    await bot.edit_message_media(media=InputMediaPhoto(media=photo,
                                                       caption=item_text),

                                 chat_id=call.message.chat.id,
                                 message_id=call.message.message_id,
                                 reply_markup=get_item_inline_keyboard(id=current_item_id))
