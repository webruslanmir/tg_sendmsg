import argparse
import telebot
import os

from dotenv import load_dotenv

# Создание парсера аргументов
parser = argparse.ArgumentParser()

# Добавление аргумента для каждой переменной
parser.add_argument('--caller_id', help='Incoming caller num')
parser.add_argument('--ext_id', default='No data', help='Income asterisk extension')
parser.add_argument('--audio_path', default='No data', help='Audio track.')


# Загрузка переменных окружения из файла .env
load_dotenv()  # take environment variables from .env.


# Разбор аргументов из командной строки
args = parser.parse_args()
CALLER_ID = args.caller_id
EXTENSION_ID = args.ext_id
AUDIO_PATH = args.audio_path

# # Использование переменных окружения
TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


bot = telebot.TeleBot(TOKEN)


def send_telegram_message(CALLER_ID, EXT_ID):
    """
    В дальнейшем планируется прослеживаемость
    факта ответа на звонок и передача информации о ответившем абоненте
    """
    if EXT_ID != 'No data':
        text = f'Входящий звонок от { CALLER_ID } на { EXT_ID }'
    else:
        text = f'Входящий звонок от {CALLER_ID}'
    bot.send_message(CHAT_ID, text)


def send_telegram_audio(audio_path):
    '''Передать путь до аудиодорожки'''
    audio = open(audio_path, 'rb')
    bot.send_audio(CHAT_ID, audio)
    audio.close()


def send_telegram_file(file_path, CALLER_ID, EXTENSION_ID):
    """
    Отправить файл с комментарием
    """
    text = f'Входящий звонок от {CALLER_ID} на {EXTENSION_ID}'
    file = open(file_path, 'rb')
    bot.send_document(CHAT_ID, file, caption=text)
    file.close()

# def send_telegram_message(CALLER_ID):
#     text = f'Входящий звонок от { CALLER_ID }'
#     bot.send_message(CHAT_ID, text)


if '__main__' == __name__:
    if AUDIO_PATH != 'No data':
        send_telegram_file(AUDIO_PATH, CALLER_ID, EXTENSION_ID)
    else:
        send_telegram_message(CALLER_ID, EXTENSION_ID)
