import json
import asyncio

from aiogram.filters import CommandStart, Command
from aiogram import types, Dispatcher, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
import config
import parse_bibl as pb

bot = Bot(token=config.TOKEN)
dp = Dispatcher()


# функция старта
@dp.message(Command("start"))
async def welcome(message: types.Message):

    kb = [[KeyboardButton(text= 'Заправки')]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard= True)

    await message.answer('Привет', reply_markup=keyboard)




# Разгаворная часть
@dp.message()
async def lalala(message: types.Message):

    if message.text == 'Заправки':

        btns = [[InlineKeyboardButton(text= "WOG", callback_data='WOG'), InlineKeyboardButton(text= "Okko", callback_data='OKKO')],
                [InlineKeyboardButton(text= "Shell", callback_data='SHELL'), InlineKeyboardButton(text= "Другие", callback_data='other')]]

        markup = InlineKeyboardMarkup(inline_keyboard= btns)
        await bot.send_message(message.chat.id, 'Список добавленых заправок', reply_markup=markup)

    elif message.text.lower() == 'пока':
        await bot.send_message(message.chat.id, 'Пока')

    else:
        await bot.send_message(message.chat.id, "Эта комманда еще не добавлена")


# Ответы на инлайновую клавиатуру

@dp.callback_query(lambda c: True)
async def good_react(call: types.callback_query):
    '''ОТветы на клавиатуру'''
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
                await bot.send_message(call.message.chat.id, 'Другие заправки еще не добавлены')
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вывожу данные по заправке:', reply_markup=None)
    except Exception as e:
        print(repr(e))


# запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

