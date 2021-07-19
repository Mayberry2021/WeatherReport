import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from main import *

with open(r"C:\Users\pllab\Desktop\MyProgram\MyProgram\WeatherReport\telegram_api_key.txt","r",encoding='utf-8') as file:
	token = file.readline()

wp = Weather_Report()

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="기상정보 챗봇입니다! /help 명령어를 통해 챗봇 사용법을 빠르게 익혀보세요!")

def help(update, context):
	show_text = "/menu 명령어를 통해 열람할 수 있는 정보를 살펴볼 수 있습니다!" + '\n' + '확인하고자 하는 정보 목록의 번호와 확인하고자 하는 지역 이름을 입력하시면 됩니다.' + '\n' + '예시) 1 부산' + '\n' + '열람할 수 있는 지역 목록은 서울, 부산, 대구, 광주, 전주, 대전, 청주, 강릉, 제주입니다!'
	context.bot.send_message(chat_id=update.effective_chat.id, text=show_text)

def menu(update, context):
	show_text = '확인하고 싶은 정보를 입력해주세요!'+ '\n' + '1. 기상정보목록' + '\n' + '2. 기상정보문' + '\n' + '3. 기상특보목록' + '\n' + '4. 기상특보문'
	context.bot.send_message(chat_id=update.effective_chat.id, text=show_text)

start_handler = CommandHandler('start', start)
menu_handler = CommandHandler('menu', menu)
help_handler = CommandHandler('help', help)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(menu_handler)
dispatcher.add_handler(help_handler)

def Select_Info(update, context):
	user_id = update.effective_chat.id
	user_text = update.message.text.split(" ")
	try:
		if user_text[0] == "1": # (번호)
			answer = wp.getWthrInfoList(user_text[1])
			context.bot.send_message(chat_id = user_id, text = answer)
		elif user_text[0] == "2":
			answer = wp.getWthrInfo(user_text[1])
			context.bot.send_message(chat_id = user_id, text = answer)
		elif user_text[0] == "3":
			answer = wp.getWthrBrkNewsList(user_text[1])
			context.bot.send_message(chat_id = user_id, text = answer)
		elif user_text[0] == "4":
			answer = wp.getWthrBrkNews(user_text[1])
			context.bot.send_message(chat_id = user_id , text = answer)
	except telegram.error.BadRequest:
		context.bot.send_message(chat_id = user_id, text = "챗봇이 이해할 수 없는 메세지입니다! /help 명령어를 통해 메세지 사용법을 확인해보세요!")

echo_handler = MessageHandler(Filters.text & (~Filters.command), Select_Info)

dispatcher.add_handler(echo_handler)

updater.start_polling()
