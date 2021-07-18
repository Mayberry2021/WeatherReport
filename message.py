from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from main import *

with open(r"C:\Users\user\Desktop\MyProgram\MyProgram\WeatherReport\telegram_api_key.txt","r",encoding='utf-8') as file:
	token = file.readline()

wp = Weather_Report()

# 새로운 메세지 왔는지 확인(Polling)
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

## 명령어 처리
# 챗봇이 수행할 실질적 기능
def start(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="기상정보 챗봇입니다! /menu 명령어로 어떤 정보들을 확인할 수 있는지 살펴보세요!")

def menu(update, context):
	show_text = '확인하고 싶은 정보를 입력해주세요!'+ '\n' + '1. 기상정보목록' + '\n' + '2. 기상정보문' + '\n' + '3. 기상특보목록' + '\n' + '4. 기상특보문'
	context.bot.send_message(chat_id=update.effective_chat.id, text=show_text)

def help(update, context):
	show_text = "/menu 명령어를 통해 열람을 원하는 메뉴 번호와 지역 이름을 입력하세요."
	context.bot.send_message(chat_id=update.effective_chat.id, text=show_text)


# 챗봇이 기능을 수행할 수 있도록 함
start_handler = CommandHandler('start', start)
menu_handler = CommandHandler('menu', menu)
help_handler = CommandHandler('help', help)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(menu_handler)
dispatcher.add_handler(help_handler)

## 메세지 처리
def WeatherInfoList(update, context):
	user_id = update.effective_chat.id
	user_text = update.message.text
	answer = wp.getWthrInfoList(user_text)
	context.bot.send_message(chat_id=user_id, text = answer)
	
def ShowWeatherInfo(update, context):
	user_id = update.effective_chat.id
	user_text = update.message.text
	answer = wp.getWtherinfo(user_text)
	context.bot.send_message(chat_id=user_id, text = answer)


echo_handler = MessageHandler(Filters.text & (~Filters.command),WeatherInfoList)
echo_handler2 = MessageHandler(Filters.text & (~Filters.command), ShowWeatherInfo)
echo_handler3 = MessageHandler(Filters.text & (~Filters.command), Select_Info)

dispatcher.add_handler(echo_handler)
dispatcher.add_handler(echo_handler2)
dispatcher.add_handler(echo_handler3)

#polling
updater.start_polling()
