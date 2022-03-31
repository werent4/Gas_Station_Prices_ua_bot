import json
import random

from aiogram import types, executor, Dispatcher, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import config
import parse_bibl as pb

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


# функция старта

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    sti = open('stikers\\hi_stiker.tgs', 'rb')
    await bot.send_sticker(message.chat.id, sti)

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    item_1 = KeyboardButton('Заправки')
    #item_2 = KeyboardButton('Случайное число')

    markup.add(item_1)

    await bot.send_message(message.chat.id, 'Привет', reply_markup=markup)


# Разгаворная часть

@dp.message_handler(content_types=['text'])
async def lalala(message: types.Message):
    #if message.text == 'Случайное число':
        #await bot.send_message(message.chat.id, str(random.randint(0, 100)))

    if message.text == 'Заправки':

        markup = InlineKeyboardMarkup(row_width=2)
        item_1 = InlineKeyboardButton("WOG", callback_data='WOG')
        item_2 = InlineKeyboardButton("Okko", callback_data='OKKO')
        item_3 = InlineKeyboardButton("Shell", callback_data='SHELL')
        item_4 = InlineKeyboardButton("Другие", callback_data='other')

        markup.add(item_1, item_2, item_3, item_4)

        await bot.send_message(message.chat.id, 'Список добавленых заправок', reply_markup=markup)

    elif message.text.lower() == 'пока':
        await bot.send_message(message.chat.id, 'Пока')

    else:
        await bot.send_message(message.chat.id, "Эта комманда еще не добавлена")

# Ответы на инлайновую клавиатуру

@dp.callback_query_handler(lambda c: True)
async def good_react(call: types.callback_query):
    '''ОТветы на клавиатуру'''
    puck = { 1 : open('audio\\puck.ogg', 'rb'),
             2 : open('audio\\puck_anton.ogg', 'rb'),
             3 : open('audio\\puck_vlad.ogg', 'rb')
            }
    try:
        if call.message:
            """ Выбор заправки"""
            if call.data == 'WOG':
                '''Для WOG'''
                pb.parse_refueling(gas_station_name='wog/')
                await bot.send_message(call.message.chat.id, 'WOG')
                ''' отправка спарсиных данных '''
                with open('refueling_data') as wog_json:
                    oil_wog_dict = json.load(wog_json)

                    for k, v in oil_wog_dict.items():
                        oil_wog_title = v['title']
                        oil_wog_price = v['price']
                        oil_wog_title_formated = ''.join(oil_wog_title)
                        oil_wog_price_formated = ''.join(oil_wog_price)
                        oil_wog =  str(oil_wog_title_formated) + ':' + str(
                            oil_wog_price_formated) + ' ' + 'грн/л'
                        await bot.send_message(call.message.chat.id, oil_wog)

            elif call.data == 'OKKO':
                '''Для OKKO'''
                pb.parse_refueling(gas_station_name='okko/')
                await bot.send_message(call.message.chat.id, 'Okko')
                ''' отправка спарсиных данных '''
                with open('refueling_data') as wog_json:
                    oil_wog_dict = json.load(wog_json)

                    for k, v in oil_wog_dict.items():
                        oil_wog_title = v['title']
                        oil_wog_price = v['price']
                        oil_wog_title_formated = ''.join(oil_wog_title)
                        oil_wog_price_formated = ''.join(oil_wog_price)
                        oil_wog =  str(oil_wog_title_formated) + ':' + str(
                            oil_wog_price_formated) + ' ' + 'грн/л'
                        await bot.send_message(call.message.chat.id, oil_wog)
            elif call.data == 'SHELL':
                '''Для SHELL'''
                pb.parse_refueling(gas_station_name='shell/')
                await bot.send_message(call.message.chat.id, 'Shell')
                ''' отправка спарсиных данных '''
                with open('refueling_data') as wog_json:
                    oil_wog_dict = json.load(wog_json)

                    for k, v in oil_wog_dict.items():
                        oil_wog_title = v['title']
                        oil_wog_price = v['price']
                        oil_wog_title_formated = ''.join(oil_wog_title)
                        oil_wog_price_formated = ''.join(oil_wog_price)
                        oil_wog =  str(oil_wog_title_formated) + ':' + str(
                            oil_wog_price_formated) + ' ' + 'грн/л'
                        await bot.send_message(call.message.chat.id, oil_wog)

            elif call.data == 'other':
                puck_choose =  random.randint(1,3)
                await bot.send_audio(call.message.chat.id, puck[puck_choose])
                await bot.send_message(call.message.chat.id, 'Другие заправки еще не добавлены')
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вывожу данные по заправке:', reply_markup=None)
    except Exception as e:
        print(repr(e))


# запуск бота
executor.start_polling(dp)

