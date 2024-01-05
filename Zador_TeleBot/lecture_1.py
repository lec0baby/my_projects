import telebot
import webbrowser


bot = telebot.TeleBot('6982935311:AAGum67M_3PtOn75C_0TiYs_KctaAmyrnTs')


# Пример того, как с помощью команды открыть сайт (почему-то открывает сайт только на моём ПК, хотя боту пишу с других устройств)

@bot.message_handler(commands=['vk'])
def open_website(message):
    webbrowser.open('https://vk.com/zzaddorr')


# Примеры обработки команд /'Что-то там'

@bot.message_handler(commands=['start', 'hello', 'hi'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, приветствую👋')

@bot.message_handler(commands=['help', 'sos'])
def send_help(message):
    bot.send_message(message.chat.id, '<b>Лист помощи</b> <em><u>Скоро сделаем!</u></em>',  parse_mode='html')

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.send_message(message.chat.id, message)


# Примеры обработки обычного текста, т.е. без /

@bot.message_handler()
def send_welcome(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, приветствую👋')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)