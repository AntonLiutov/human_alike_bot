import constants as keys
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import responses as r

print("Bot started...")


def start_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        """
        Hello sir, Welcome to the Bot.Please write
        /help to see the commands available.
        """)


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"""Sorry '{update.message.text}' is not a valid command""")


def handle_message(update, context):
    print(update.message)
    text = str(update.message.text).lower()
    response = r.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")
    update.message.reply_text("Sorry, I need to get rest for a while. Please, text me in 1 hour")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    # dp.add_handler(CommandHandler('start', start_command))

    # dp.add_handler(MessageHandler(Filters.command, unknown))  # Filters out unknown commands
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
