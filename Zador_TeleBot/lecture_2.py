import telebot
from telebot import types

bot = telebot.TeleBot('6982935311:AAGum67M_3PtOn75C_0TiYs_KctaAmyrnTs')


# Пример создания статичных кнопок

@bot.message_handler(commands=['start'])
def static(message):
    markup = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('Кнопка №1')
    markup.row(button1)
    button2 = types.KeyboardButton('Кнопка №2')
    button3 = types.KeyboardButton('Кнопка №3')
    markup.row(button2, button3)
    file = open('./photo.jpg', 'rb')                              # Отправка фото от бота (файл в папке с кодом)
    bot.send_photo(message.chat.id, file, reply_markup=markup)
#    bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, press_button)     # Действия со статичными кнопками

def press_button(message):
    if message.text == 'Кнопка №1':
        bot.send_message(message.chat.id, 'Скоро в продаже')
    elif message.text == 'Кнопка №2':
        bot.send_message(message.chat.id, 'В наличии')
    elif message.text == 'Кнопка №3':
        bot.send_message(message.chat.id, 'Осталось совсем мало размеров')

# Пример обработки разных типов сообщений: фото, аудио, видео, голосовые сообщения

@bot.message_handler(content_types=['video', 'audio', 'document', 'sticker'])
def get_any(message):
    bot.reply_to(message, 'Годно!')


# Пример добавления кнопок к сообщению

@bot.message_handler(content_types=['voice'])
def get_vocie(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на группу', url='https://vk.com/zzaddorr'))
    markup.add(types.InlineKeyboardButton('Удалить фото'))
    markup.add(types.InlineKeyboardButton('Изменить текст'))
    bot.reply_to(message, 'Чётко делаешь!', reply_markup=markup)


# Пример расположения кнопок

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Перейти на группу', url='https://vk.com/zzaddorr')
    markup.row(button1)             # Заполняем первый ряд какими-либо кнопками
    button2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    button3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(button2, button3)            # Заполняем второй ряд какими-либо кнопками
    bot.reply_to(message, 'Зачётный прикид!)', reply_markup=markup)

# Создание функций callback (действие кнопки)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text',callback.message.chat.id, callback.message.message_id)


bot.polling(none_stop=True)