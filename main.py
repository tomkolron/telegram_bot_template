import telebot

API_KEY = 'YOUR API KEY'
bot = telebot.TeleBot(API_KEY)

command = 'THE NAME OF YOUR COMMAND'

@bot.message_handler(commands=[command])
def greet(massage) :
    msg = str(massage.text).replace('/' + command, '').strip()
    if msg == '':
        bot.reply_to(massage, 'type in a password after the colon')
    else:
        # code to process the message here

        response = 'YOUR RESPONSE'
        bot.reply_to(massage, response)

bot.polling()