import logging
from typing import List

import telebot
import telebot.types as types

import app.config as config

bot = telebot.TeleBot(config.TOKEN)
log = logging.getLogger(__name__)


def start():
    bot.set_my_commands(_get_commands())
    bot.polling(none_stop=True)


@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.send_message(message.chat.id,
                     f"Привет! Иди в Жопу!")





def _get_commands() -> List[types.BotCommand]:
    return [

    ]
