from aiogram import types
from aiogram.types import InputFile,InputMediaPhoto

from keyboards_paket import get_item_inline_keyboard,navigation_items_callback,item_count_callback,basket_callback,basket_keyboard
from loader import db,dp,bot

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

@dp.callback_query_handler(item_count_callback.filter(target='item_plus'))
async def plus_item(call: types.CallbackQuery):
    current_count = int(call.data.split(':')[-1])
    current_item_id = int(call.data.split(':')[-2])
    item_info = db.select_item_info(id=current_item_id)
    item_info = item_info[0]
    _,name,count,path_to_photo = item_info
    if current_count != count:
        current_count += 1
        item_text = f'Название товара: {name}'\
                    f'\nКолическтво товара: {count}'
        photo = InputFile(path_or_bytesio=path_to_photo)
        await bot.edit_message_media(media=InputMediaPhoto(media=path_to_photo,
                                                            caption=item_text),
                                                            chat_id=call.message.chat.id,
                                                            message_id=call.message.message_id,
                                                            reply_markup=get_item_inline_keyboard(id=current_item_id,
                                                            current_count=current_count))
                                            

@dp.callback_query_handler(item_count_callback.filter(target='item_minus'))
async def plus_item(call: types.CallbackQuery):
    current_count = int(call.data.split(':')[-1])
    current_item_id = int(call.data.split(':')[-2])
    item_info = db.select_item_info(id=current_item_id)
    item_info = item_info[0]
    _,name,count,path_to_photo = item_info
    if current_count != 1:
        current_count -= 1
        item_text = f'Название товара: {name}'\
                    f'\nКолическтво товара: {count}'
        photo = InputFile(path_or_bytesio=path_to_photo)
        await bot.edit_message_media(media=InputMediaPhoto(media=path_to_photo,
                                                            caption=item_text),
                                                            chat_id=call.message.chat.id,
                                                            message_id=call.message.message_id,
                                                            reply_markup=get_item_inline_keyboard(id=current_item_id,
                                                            current_count=current_count))


@dp.callback_query_handler(item_count_callback.filter(target='basket'))
async def add_item_basket(call: types.CallbackQuery):
    current_count = int(call.data.split(':')[-1])
    current_item_id = int(call.data.split(':')[-2])
    user_id,user_basket = db.select_user_basket(id=call.from_user.id)
    user_basket = [item_data.split(':') for item_data in user_basket.split()]

    for i in range(len(user_basket)):
        item_id, item_count = user_basket[i]
        if current_item_id == item_id:
            user_basket[i][1] = str(int(item_count) + current_count)
            break
        else:
            user_basket += [[current_item_id, str(current_count)]]
        user_basket = ' '.join([':'.join(dbl) for dbl in user_basket])
        db.update_basket(id=user_id, user_basket=user_basket)
        await bot.answer_callback_query(callback_query_id=call.id,
                                        text='Товар успешно добавлен.',
                                        show_alert=False)
