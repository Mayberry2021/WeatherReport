from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from main import *

with open(r"C:\Users\pllab\Desktop\MyProgram\MyProgram\WeatherReport\telegram_api_key.txt","r",encoding='utf-8') as file:
	token = file.readline()

wp = Weather_Report()

# 새로운 메세지 왔는지 확인(Polling)
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

## 명령어 처리
# 챗봇이 수행할 실질적 기능
def start(update, context):
	print(update.effective_chat.id)
	context.bot.send_message(chat_id=update.effective_chat.id, text="기상정보 챗봇입니다!")

# 챗봇이 기능을 수행할 수 있도록 함
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

#def show_Weather_Info_List(update, context):
#	context.bot.send_message(chat_id=update.effectiove_chat.id)
#	getWthrInfoList()

## 메세지 처리
#def echo(update, context):
#	user_id = update.effective_chat.id
#	user_text = update.message.text
#	answer = wp.
#	context.bot.send_message(chat_id=user_id, text = "안녕")
	
#echo_handler = MessageHandler(Filters.text & (~Filters.command),echo)


dispatcher.add_handler(echo_handler)

#polling
updater.start_polling()
