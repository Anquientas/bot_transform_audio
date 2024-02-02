from dotenv import load_dotenv
import speech_recognition
import telebot
from pydub import AudioSegment

import os


load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

recognizer = speech_recognition.Recognizer()

GREETINGS = 'Привет, {name}!'


def oga_transform_to_wav(filename):
    """Функция конвертации формата *.oga в *.wav."""
    new_filename = filename.replace('.oga', '.wav')
    audio = AudioSegment.from_file(filename)
    audio.export(new_filename, format='wav')
    return new_filename


def recognize_speech(filename_oga):
    """Функция перевода голоса в текст."""
    filename_wav = oga_transform_to_wav(filename_oga)
    recognizer = speech_recognition.Recognizer()

    with speech_recognition.WavFile(filename_wav) as source:
        wav_audio = recognizer.record(source)
    text = recognizer.recognize_google(wav_audio, language='ru')

    if os.path.exists(filename_oga):
        os.remove(filename_oga)
    if os.path.exists(filename_wav):
        os.remove(filename_wav)
    return text


def download_file(bot, file_id):
    """Функция скачивания файла, присланного пользователем."""
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    filename = (file_id + file_info.file_path).replace('/', '_')
    with open(filename, 'wb') as file:
        file.write(downloaded_file)
    return filename


@bot.message_handler(content_types=['voice'])
def transcript(message):
    """Функция отправки текста в отмет на голосовое сообщение."""
    filename = download_file(bot, message.voice.file_id)
    text = recognize_speech(filename)
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['start'])
def greetings(message):
    """Функция отправки приветственного сообщения."""
    bot.send_message(
        message.chat.id,
        GREETINGS.format(name=message.chat.first_name)
    )


def main():
    bot.polling()


if __name__ == '__main__':
    main()
