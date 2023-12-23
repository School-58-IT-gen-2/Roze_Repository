from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
from telegram.ext import CallbackContext
from typing import List


def start(update: Update, context: CallbackContext):
    update.message.reply_text("привет")

def send_response_to_player(update: Update, context: CallbackContext, response: str):
				update.message.reply_text(response)

def get_request_from_player(update: Update, context: CallbackContext, button_func: dict):
				custom_keyboard = [[*button_func.keys()]]
				reply_markup = ReplyKeyboardMarkup(custom_keyboard)
				update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)
				button_click(update, context, button_func)

def button_click(update: Update, context: CallbackContext):
				text = update.message.text
				if text in button_func:
								button_func[text](update, context)
				else:
								update.message.reply_text("Пожалуйста, выберите опцию из предложенных кнопок.")

updater = Updater("6068101345:AAGr0hpElzAEBwfoc7-yoUhd-QRD9Sd8vr4")  # Замените "YOUR_BOT_TOKEN" на реальный токен вашего бота
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, button_click))

updater.start_polling()



#ПРИМЕР МИШИ
'''
from telegram import Bot


token = "6068101345:AAGr0hpElzAEBwfoc7-yoUhd-QRD9Sd8vr4"
bot = Bot(token=token)

class TelegramView:
    def __init__(self) -> None:
        self.update_id = None

    def request(self, chat_id: int = None, text: str = None):
        if text is not None:
            bot.send_message(chat_id, text)
        
        while True:
            updates = bot.get_updates(offset=self.update_id, timeout=10000)
            for update in updates:
                if update.message is not None and update.message.text is not None:
                    self.update_id = update.update_id + 1
                    return update.message.text



a = TelegramView()
while True:
    print(a.request())

'''