import logging
import os
import tables
import random

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

from filters import FilterCooking

from sqlalchemy import select


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Привіт! "
                                  "Я допоможу тобі вирішити, що приготувати. "
                                  "Напиши 'що приготувати?' "
                                  "або тисни на кнопку."
                             )


def cook(update: Update, context: CallbackContext):
    ids = tables.session.execute(select(tables.Recipe.id))
    ids = [dict(row) for row in ids]
    recipe_id = random.choice(ids)['id']
    recipe = [dict(row) for row in tables.session.execute(
        select(tables.Recipe.name)
        .where(tables.Recipe.id == recipe_id)
    )]
    context.bot.send_message(chat_id=update.effective_chat.id, text=recipe[0]['name'])


def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Вибач, я не знаю, що це означає.")


def main():
    filter_cooking = FilterCooking()

    updater = Updater(token=os.environ.get('TOKEN'))
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    cook_handler = CommandHandler('cook', cook)
    dispatcher.add_handler(cook_handler)

    cooking_handler = MessageHandler(filter_cooking & (~Filters.command), cook)
    dispatcher.add_handler(cooking_handler)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
