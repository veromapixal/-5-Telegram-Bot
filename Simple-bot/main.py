import telebot
from telebot import types
token = '2127335451:AAG4A_E4dVUNn8V8hQYBK4vWlC3pxaVrV5s'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])


def start(message):
    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('ПН ВЕРХ', 'ПН НИЗ')
    keyboard.row('ВТ ВЕРХ', 'ВТ НИЗ')
    keyboard.row('СР ВЕРХ', 'СР НИЗ')
    keyboard.row('ЧТ ВЕРХ', 'ЧТ НИЗ')
    keyboard.row('ПТ ВЕРХ', 'ПТ НИЗ')
    keyboard.row('СБ ВЕРХ', 'СБ НИЗ')
    keyboard.row('/help')
    bot.send_message(message.chat.id, 'Привет, я - бот с расписанием для группы БВТ2105. Какой день недели тебя интересует?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею показывать расписание на выбранный день недели. В разработке - команда для связи с преподавателями и ссылками на ЭИОС и расписание в формате таблицы.')


@bot.message_handler(content_types=['text'])
def main(message):
    id = message.chat.id
    msg = message.text
    if msg == 'ПН ВЕРХ' or msg == 'ПН НИЗ':
        bot.send_message(id, '11:25 - КГ практика - скинуть работы; '
                             '15:25 - ВТ практика; '
                             '17:10 - Философия практика; '
                             '19:00 - ВвИТ практика ')

    elif msg == 'ВТ ВЕРХ':
        bot.send_message(id, 'чилл')
        bot.send_message(id, 'https://a.d-cd.net/g6AAAgN1PeA-1920.jpg')

    elif msg == 'ВТ НИЗ':
        bot.send_message(id, '11:25 - физра; '
                             '13:10 - ВвИТ лаб; '
                             '15:25 - ВвИТ лаб; '
                             '17:10 - ВвИТ лекция ')

    elif msg == 'СР ВЕРХ':
        bot.send_message(id, '11:25 - физра; '
                             '13:10 - Философия лекция; '
                             '15:25 - КГ лекция ')

    elif msg == 'СР НИЗ':
        bot.send_message(id, '9:30 - Английский; '
                             '11:25 - Английский ')

    elif msg == 'ЧТ ВЕРХ':
        bot.send_message(id, '11:25 - физра; '
                             '15:25 - ВысшМат лекция; '
                             '17:10 - АГиЛА лекция ')

    elif msg == 'ЧТ НИЗ':
        bot.send_message(id, '11:25 - ИЭ лекция; '
                             '15:25 - ИЭ лаб; '
                             '17:10 - физра ')

    elif msg == 'ПТ ВЕРХ' or msg == 'ПТ НИЗ':
        bot.send_message(id, '11:25 - ВТ лекция ')

    elif msg == 'СБ ВЕРХ' or msg == 'СБ НИЗ':
        bot.send_message(id, '9:30 - ВысшМат; '
                             '11:25 - АГиЛА ')




bot.infinity_polling(none_stop=True)
