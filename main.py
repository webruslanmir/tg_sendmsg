import argparse
import telebot
import os

from dotenv import load_dotenv

# Создание парсера аргументов
parser = argparse.ArgumentParser()

# Добавление аргумента для каждой переменной
parser.add_argument('--caller_id', help='Номер звонящего')
parser.add_argument('--called_id', default='No data', help='Call to...')

# Разбор аргументов из командной строки
args = parser.parse_args()
CALLER_ID = args.caller_id
CALLED_ID = args.called_id

# Загрузка переменных окружения из файла .env
load_dotenv()  # take environment variables from .env.


# # Использование переменных окружения
TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

bot = telebot.TeleBot(TOKEN)


# def send_telegram_message(CALLER_ID, CALLED_ID):
# '''В дальнейшем планируется прослеживаемость факта ответа на звонок и передача информации о ответившем абоненте'''
#     text = f'Входящий звонок от { CALLER_ID } адресован для { CALLED_ID }'
#     bot.send_message(CHAT_ID, text)


def send_telegram_audio(audio_path):
    '''Передать путь до аудиодорожки'''
    audio = open(audio_path, 'rb')
    bot.send_audio(CHAT_ID, audio)
    audio.close()


def send_telegram_message(CALLER_ID):
    text = f'Входящий звонок от { CALLER_ID }'
    bot.send_message(CHAT_ID, text)


if '__main__' == __name__:
    send_telegram_message(CALLER_ID)
