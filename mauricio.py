from telegram.ext import Updater, CommandHandler
from keys import BOT_TOKEN, FILE_PATH

# import requests
import json
import re
import random

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

def main():
    updater = Updater(BOT_TOKEN)
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('fala_mauricio', say_it))

    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()