import telebot
from fluent import sender
from fluent import event
sender.setup('fluentd.bot', host='localhost', port=8080)

API_TOKEN = "**YOUR_API_TOKEN**"

bot = telebot.TeleBot(API_TOKEN)

# Define a command handler
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    event.Event('start message', {
        'user_id': message.from_user.id,
        'user_name':   message.from_user.username
        })
    bot.reply_to(message, "Welcome to YourBot! Type /info to get more information.")

@bot.message_handler(commands=["info"])
def send_info(message):
    bot.reply_to(message, "This is a simple Telegram bot for lab3.")

# Define a message handler
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text.startswith("danger"):
        event.Event('error', { 
            'user_id': message.from_user.id,
            'user_name':   message.from_user.username,
            'user_message': message.text})
        bot.reply_to(message, message.text+ " is eliminated!")
    else:
        bot.reply_to(message, message.text+ " lab3!")
# Start the bot
bot.polling()
