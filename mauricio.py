from flask import Flask
from telegram.ext import Updater, CommandHandler
from keys import BOT_TOKEN, FILE_PATH
from utils import DECISION_LIST, NAMES

import json
import random


app = Flask(__name__)


def parse_quotes(file_path):
    quotes_list = list()

    with open(file_path) as quotes_file:
        quotes_dict = json.load(quotes_file)

        for k, quote in quotes_dict[0].items():
            quotes_list.append(quote)

        return quotes_list

QUOTES_LIST = parse_quotes(FILE_PATH)
def get_random_quote():
    return random.choice(QUOTES_LIST)

def say_it(bot, update):

    chat_id = update.message.chat_id
    random_quote = get_random_quote()

    bot.send_message(chat_id=update.effective_chat.id, text=random_quote)

def decide(bot, update):
    chat_id = update.message.chat_id
    decision = random.choice(DECISION_LIST)

    bot.send_message(chat_id=update.effective_chat.id, text=decision)


def choose(bot, update):
    chat_id = update.message.chat_id
    option = random.choice(NAMES)

    bot.send_message(chat_id=update.effective_chat.id, text=option)


@app.route('/')
def lets_goo():
    updater = Updater(BOT_TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('fala_mauricio', say_it))
    dp.add_handler(CommandHandler('decide_mauricio', decide))
    dp.add_handler(CommandHandler('escolhe_mauricio', choose))

    updater.start_polling()
    updater.idle()


while True:
    lets_goo()