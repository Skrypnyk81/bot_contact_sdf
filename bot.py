import telebot
from telebot.types import Message
import pandas as pd
from credential import *


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Ciao, per iniziare la ricerca digita cognome e/o nome")

@bot.message_handler(content_types=['text'])
def contact_risponce(message: Message):
    file = pd.read_csv('data_contact.csv')
    request = message.text.upper()
    answer  = file[file['COGNOME E NOME'].str.contains(request)].to_string(index=False)
    bot.send_message(message.chat.id, answer)


bot.polling(timeout=60)
