# Приветствие + стикер
# Пожалуйста выберите валюту (eth/btc/выход) + inline keyboard
# Пожалуйста выберите (новости/катировки на рынке на текущий момент/выход) + inline keyboard
# Высылаем новости/цену на рынке или если нажимает "выход", то прощаемся + inline keyboard
# Прощание + стикер 
# Даём доступ другим пользователям
# Выложить на гидхабе

import telebot

from telebot import types

import requests

from bs4 import BeautifulSoup

token = '1831524983:AAGX9JzqSODryG6VKO6jtjWnZmPsCpbsR5A'

bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['start']) # Приветствие + стикер
# def welcome(message):
#     sti = open('sticker.webp', 'rb')
#     bot.send_sticker(message.chat.id, sti)

#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # Нижняя клавиатура (часть функции выше)
#     item1 = types.KeyboardButton("Bitcoin")
#     item2 = types.KeyboardButton("Ethereum")
#     item3 = types.KeyboardButton("Выход")

#     markup.add(item1, item2, item3)

#     bot.send_message(message.chat.id, "Добро пожаловать в Crypto News Bot! Пожалуйста выберите валюту: ", reply_markup = markup)
# # reply_markup = markup подкрепляет клавиатуру к ответу

# @bot.message_handler(content_types=['text'])
# def question_1(message):
#     if message.chat.type == "private":
#         if message.text == "Bitcoin":
#             # Инлайновая клавиатура
#             markup = types.InlineKeyboardMarkup(row_width=2)
#             item1 = types.InlineKeyboardButton("Акутальная цена на рынке", callback_data= 'price')
#             item2 = types.InlineKeyboardButton("3 последние новости", callback_data= 'news')
            
#             markup.add(item1, item2)
#             # reply_markup = markup подкрепляет клавиатуру к ответу
#             bot.send_message(message.chat.id, "Вы выбрали Bitcoin. Выберите следующиее: ", reply_markup = markup)
#         elif message.text == "Ethereum":

#             markup = types.InlineKeyboardMarkup(row_width=2) # Инлайновая клавиатура
#             item1 = types.InlineKeyboardButton("Акутальная цена на рынке", callback_data= 'price')
#             item2 = types.InlineKeyboardButton("3 последние новости", callback_data= 'news')

#             markup.add(item1, item2)
#             # reply_markup = markup подкрепляет клавиатуру к ответу
#             bot.send_message(message.chat.id, "Вы выбрали Ethereum. Выберите следующиее: ", reply_markup = markup)
#         elif message.text == "Выход":
#             bot.send_message(message.chat.id, "Всего хорошего!")
#         else:
#             bot.send_message(message.chat.id, "Пожалуйста, выберите что-то из доступных опций")

# # Обработка нажатия на кнопку инлайновой клавиатуры. Делается это уже при помощи отдельного метода и 
# # отдельного декоратора
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     try:
#         if call.message:
#             if call.data == "price":
#                 bot.send_message(call.message.chat.id, "***Высылаем цену на рынке***")
#             elif call.data == "news":
#                 bot.send_message(call.message.chat.id, "***Высылаем новости***")
#             else:
#                 bot.send_message(call.message.chat.id, "***Пожалуйста выберите что-то из доступных опций***")
            
#             # удаляем инолайн клавиатуру после того, как юзер выбереит одну из опций
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Данная опция была выбрана", reply_markup=None)

#             # создаём уведомление (show alert) при помощи answer.callbeck.query
#             bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False, text="Это тестовое уведомление")

#     except Exception as e:
#         print(repr(e))

# bot.polling(none_stop = True)

# ЧАСТЬ С ВЫСЫЛКОЙ НОВОСТЕЙ

@bot.message_handler(content_types = ['text'])
def handle(message):
	URL = 'https://pl.investing.com/'
	HEADERS = {
		'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
	}

	response = requests.get(URL, headers = HEADERS)
	soup = BeautifulSoup(response.content, 'html.parser')
	texts = soup.findAll('span', 'ob-unit.ob-rec-text')

	for i in range(len(texts[:-5]), -1, -1):
		txt = str(i + 1) + ') ' + texts[i].text
		bot.send_message(message.chat.id, '<a href="{}">{}</a>'.format(texts[i]['href'], txt), parse_mode = 'html')

bot.polling(none_stop = True)