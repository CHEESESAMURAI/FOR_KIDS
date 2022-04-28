from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputFile
import requests

import config
import markups as kb

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

file_id = 0

opisanie=[]

ras1 = 0
ras = []

@dp.message_handler(commands=['start'])
async def start_cmd(msg: types.Message):
    user_name = msg.from_user.username
    id = msg.chat.id
    await bot.send_message(id,'Здравствуйте ,' + str(user_name)+'!\n Я чат-бот магазина Arina shop 😇 \n Как я могу вам помочь?💖',reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message_id)


@dp.message_handler(commands=['setpic'])
async def start_cmd(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Отправьте картинку для обновления !')
    await bot.delete_message(msg.from_user.id, msg.message_id)


@dp.message_handler(commands=['mailing'])
async def start_cmd(msg: types.Message):
    global ras1
    if msg.from_user.id == 1659228199:
        ras1 = 1
    await bot.delete_message(msg.from_user.id, msg.message_id)

@dp.message_handler(content_types=["photo"])
async def get_photo(message):
    global file_id
    if message.from_user.id == 1659228199:
        file_id = message.photo[-1].file_id
        print(file_id) # этот идентификатор нужно где-то сохранить
        await bot.delete_message(message.from_user.id, message.message_id)
    else:
        await bot.delete_message(message.from_user.id, message.message_id)


@dp.callback_query_handler(text='menu')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,'Выберите дейтсвие которое вам нужно :',reply_markup=kb.menu2)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    await bot.delete_message(msg.from_user.id, msg.message.message_id - 1)


@dp.callback_query_handler(text='rezhim')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,'🕕Режим работы🕕\n🗓Пн : 00:00 - 24:00\n🗓Вт : 00:00 - 24:00\n🗓Ср : 00:00 - 24:00 \n🗓Чт : 00:00 - 24:00\n🗓Пт : 00:00 - 24:00\n🗓Сб : 00:00 - 24:00\n🗓Вс : 00:00 - 24:00',reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='adres')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,'📍Нажмите на геолокацию и удобный вам навигатор , он сам простроит вам маршрут до нас📍')
    await bot.send_location(id,55.753844509007045, 37.61984158321927,reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='contact')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,'📞Наши контактные данные\n1293666\nРоссия,Москва  Проспект Мира,150  \nМетроВДНХ,гостиница "Космос"  \nБизнес крыло INTOURST.\nофис 39  \nТел. +7 (495) 642-2684 \nЧасы работы: 11:00-18:00',reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='tovar')
async def menu(msg: types.Message):
    global file_id
    global opisanie
    await bot.send_photo(chat_id=msg.from_user.id,photo=file_id,caption=opisanie[0],reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='podpis')
async def menu(msg: types.Message):
    id = msg.from_user.id
    global ras

    await bot.send_message(id,'Вы успешно активировали подписку',reply_markup=kb.menu2)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


    if msg.from_user.id in ras:
        print('уже есть')
    else:
        ras.append(msg.from_user.id)

    print(ras)
@dp.callback_query_handler(text='otpodpis')
async def menu(msg: types.Message):
    id = msg.from_user.id
    global ras
    user_id = msg.from_user.id

    for i in ras:
        if i == user_id:
            ras.remove(i)
    print(ras)
    await bot.send_message(id,'Вы успешно деактивировали подписку',reply_markup=kb.menu2)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.message_handler(content_types=types.ContentTypes.ANY)
async def all_other_messages(message: types.Message):
    global ras1
    global opisanie
    if message.from_user.id == 1659228199 and ras1 == 1:
        for i in ras:
            await bot.send_message(i, message.text)
        ras1=0
        await bot.delete_message(message.from_user.id, message.message_id)
    elif message.from_user.id == 1659228199:
        opisanie.append(message.text)
        await bot.delete_message(message.from_user.id, message.message_id)
    else:
        await message.answer("Я не совсем понимаю тебя .Введите /start")
        await bot.delete_message(message.from_user.id, message.message_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
