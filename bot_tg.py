from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import requests

def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("Курс валют", callback_data='currency')]]
    update.message.reply_text('Выберите опцию:', reply_markup=InlineKeyboardMarkup(keyboard))

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == 'currency':
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()
        query.edit_message_text(f"Курс USD: {response['rates']['RUB']} RUB")

updater = Updater('YOUR_TELEGRAM_BOT_TOKEN')
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
updater.idle()
