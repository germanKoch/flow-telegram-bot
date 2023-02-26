import logging
import uuid

import telebot

import app.config as config
import pathlib

from app.until.loader import load_img, remove_img

from app.ml.flower_classifier import FlowerClassifier

bot = telebot.TeleBot(config.TOKEN)
log = logging.getLogger(__name__)
flow_classifier = FlowerClassifier()


def start():
    bot.set_my_commands(_get_commands())
    bot.polling(none_stop=True)


@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id,
                     f"Привет! Иди в Жопу!")


@bot.message_handler(content_types=['file', 'photo'])
def photo(message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)

    filename = pathlib.Path(file_info.file_path).name

    local_filename = f"{uuid.uuid1()}_{filename}"
    downloaded_file = bot.download_file(file_info.file_path)

    load_img(local_filename, downloaded_file)

    result = flow_classifier.predict(local_filename)
    bot.send_message(message.chat.id, result)

    remove_img(local_filename)


def _get_commands():
    return []
