from telebot import TeleBot, types

bot = TeleBot('8439453968:AAF4mJBdzljJTYXw4i6fjeMfVmPelfbyYVA')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Start Chatting 😎', 'Join Channel')
    markup.row('About Us')
    bot.send_message(message.chat.id, "Welcome to Anonymous Chat!", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    if message.text == 'Start Chatting 😎':
        bot.send_message(message.chat.id, "🔍 Searching for a partner...")
    elif message.text == 'Join Channel':
        bot.send_message(message.chat.id, "👉 Join our channel: https://t.me/yourchannelname")
    elif message.text == 'About Us':
        bot.send_message(message.chat.id, "We connect strangers for fun anonymous chats.")
    else:
        bot.send_message(message.chat.id, "Please choose an option from the menu.")

bot.polling()
