from telegram import Update
from telegram.ext import Updater, CommandHandler, ContextTypes
import baza



def hello(update: Update, context: ContextTypes) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


update = Updater('5763934721:AAEBodGFIV7B_OM_lehIFsvqesc7jG3LD9I')

update.dispatcher.add_handler(CommandHandler("hello", hello))
update.dispatcher.add_handler(CommandHandler("baza", baza.controler))

update.start_polling()
update.idle()