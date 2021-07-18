import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler


token = '1705576598:AAEbHpTrctEcuQTeM_ZboJE9VhZnKz2E14I'

bot = telegram.Bot(token=token)
updates = bot.getUpdates()
print(updates)