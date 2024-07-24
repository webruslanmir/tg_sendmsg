import telebot

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'

bot = telebot.TeleBot(TOKEN)


def send_telegram_message(number):
    text = f'Incoming call from number: {number}'
    bot.send_message(CHAT_ID, text)


if '__main__' == __name__:
    send_telegram_message(1)
