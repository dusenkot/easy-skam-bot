import telebot  # библиотеки
from telebot import types

bot = telebot.TeleBot('1074545272:AAF6f7JQYe7LB_SNUPF_LQ9NTrXheOIQ0eE')  # токен


@bot.message_handler(commands=['start'])  # 1блок
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Тернополь')
    item2 = types.KeyboardButton('Киев')
    item3 = types.KeyboardButton('Харьков')
    item4 = types.KeyboardButton('Ивано-Франковск')
    item5 = types.KeyboardButton('Ужгород')
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, 'Добро пожаловать в шоп с лучшими шишками. Выбери свой город:', reply_markup=markup)


@bot.message_handler(content_types=['text'])  # 2блок
def contry(message):
    if message.text =='Ужгород' or message.text=='Ивано-Франковск' or message.text == 'Тернополь' or message.text == 'Киев' or  message.text=='Харьков':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item6 = types.KeyboardButton('AK')  # 200
        item7 = types.KeyboardButton('LSD')  # 220
        item8 = types.KeyboardButton('BlueBerry')  # 210
        markup1.add(item6, item7, item8)
        var = bot.send_message(message.chat.id, 'Выбери товар:', reply_markup=markup1)
        bot.register_next_step_handler(var, cilkicst)

def cilkicst(message):
    if message.text == 'LSD':
        markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton('1гр-220грн')
        button1 = types.KeyboardButton('2гр-420грн')
        markup5.add(button,button1)
        varini = bot.send_message(message.chat.id, 'Количество', reply_markup=markup5)
        bot.register_next_step_handler(varini, gigga)
    if message.text == 'BlueBerry':
        markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton('1гр-210грн')
        button1 = types.KeyboardButton('2гр-400грн')
        markup5.add(button,button1)
        varini = bot.send_message(message.chat.id, 'Количество', reply_markup=markup5)
        bot.register_next_step_handler(varini, gigga)
    if message.text == 'AK':
        markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button = types.KeyboardButton('1гр-200грн')
        button1 = types.KeyboardButton('2гр-380грн')
        markup5.add(button,button1)
        varini = bot.send_message(message.chat.id, 'Количество', reply_markup=markup5)
        bot.register_next_step_handler(varini, gigga)
def gigga(message):
    if message.text == '1гр-200грн' or message.text == '1гр-210грн' or message.text == '1гр-220грн' or message.text == '2гр-420грн' or message.text == '2гр-380грн' or message.text == '2гр-400грн':
        markup6 = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id,'Оплата EasyPay: 68038396. Скриншот оплаты отправляем оператору @uastaff_oper и получаем адрес клада.', reply_markup=markup6)

bot.polling(none_stop=True)  # run
