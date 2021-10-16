import telebot

bot=telebot.TeleBot("1775479083:AAF77tFjgyfHdA0VZJ1nDI42AjI76-fefHg")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.reply_to(message,message.text)
bot.polling(none_stop=True)


