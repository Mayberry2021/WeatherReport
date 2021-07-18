from telegram.ext import Updater
from telegram.ext import CommandHandler

token = '1705576598:AAEbHpTrctEcuQTeM_ZboJE9VhZnKz2E14I'

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

''' 
bot = telegram.Bot(token=token)
updates = bot.getUpdates()
for u in updates:
	print(u)
'''