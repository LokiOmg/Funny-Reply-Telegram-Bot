#Funny replies telegram bot
from datetime import datetime
import logging
from module.responce import dict_quote, dict_jokes
from module.stickers import dict_stik, dict_gif
from module.confih import TOKEN
import random
import re
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import filters
#Logging messages
logging.basicConfig(format='%(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)
#Var dict's
val_quotes = list(dict_quote.keys())
val_jokes = list(dict_jokes.keys())
val_stikers = list(dict_stik)
val_gif = list(dict_gif)
rerand = random.seed(1)
#Var time
curenttime = datetime.now()
curenttime_hour = int(curenttime.strftime("%H"))
worktime_start = int(9)
worktime_end = int(19)
work_morning = int(11)
#Слова тригеры
dic_keywords = ["bot", "бот", "ботяра"]
dic_dogs = ["пёс", "пес", "псина", "песель", "песик", "пса", "псы"]
dic_opozd = ["опаздаю", "опаздываю", "теряйте", "проспал"]
dic_bolt = ["болтушка", "болтанка", "крутилка", "покрутить", "накрутка", "вертеть", "вращать"]

#Handler /start
def start(update, context):
	update.message.reply_text('Приступаю к работе')
	
#Handler /help
def help(update, context):
	update.message.reply_text('тест хелп')

#Handler /stop
def stop(update, context):
	update.message.reply_text('Мавр сделал своё дело, Мавр может уходить..')
	Bot.shutdown()

def work_time(update, context):
	choise_oit = random.choices(val_quotes, k=1)
	choiseoit_joke = random.choices(val_jokes, k=1)
	choise_stik = random.choice(val_stikers)
	choiseoit_gif = random.choice(val_gif)
	chatid = update.effective_chat.id
	text = update.message.text.lower()
	tokens = re.findall(r'\w+', text)
	if curenttime_hour >= worktime_start <= worktime_end:
		if (random.randrange(0,3) == 1):
			if any(x in dic_bolt for x in tokens):
				if (random.randrange(0,3) == 0):
					update.message.reply_text("Ооо кто-то захотел болтанки?")
					context.bot.send_document(chatid, "https://media.giphy.com/media/jItYmdPZ3YFTq/giphy.gif")
				else:
					update.message.reply_text("Болтушка подана - Сэр!")
					context.bot.send_document(chatid, "https://media.giphy.com/media/tQcjerc5JJGxi/giphy.gif")
			elif any(x in dic_dogs for x in tokens):
				min_rand = random.randrange(0,3)
				if min_rand == 0:
					update.message.reply_text("Сам ты псина!")
				elif min_rand == 2:
					update.message.reply_text("Это кто тут лает?")
				else:
					context.bot.send_document(chatid, choiseoit_gif)
			elif any(x in dic_keywords for x in tokens):
				min_rand = random.randrange(0,4)
				if min_rand == 1:
					update.message.reply_text("Может я и бот, но поумнее некоторых..")
				elif min_rand == 2:
					vol_str = ''.join(choiseoit_joke)
					update.message.reply_text(f' {vol_str}')
				else:
					context.bot.send_document(chatid, choiseoit_gif)
			else:
				mind_rad = random.randrange(0,4)
				if mind_rad == 0 or mind_rad == 1:
					vol_str1 = ''.join(choise_oit)
					update.message.reply_text(f' {vol_str1}')
				else:
					vol_str2 = ''.join(choiseoit_joke)
					update.message.reply_text(f' {vol_str2}')
		elif (random.randrange(0,3) == 3):
			context.bot.send_document(chatid, choise_stik)
		else:
			None
	elif curenttime_hour >= worktime_start <= work_morning:
		if any(x in dic_opozd for x in tokens):
			vol_str3 = ''.join(choiseoit_joke)
			update.message.reply_text(f'Опять проспал?! Вот тебе для заряда: {vol_str3}')
		else:
			if (random.randrange(0,5) == 1):
				vol_str4 = ''.join(choise_oit)
				update.message.reply_text(f'Доброго утречка! Отличный день для заявок! {vol_str4}')
			else:
				None
	else:
		if (random.randrange(0,10) == 1):
			update.message.reply_text(f'Время то не рабочее {curenttime.strftime("%H:%M")}!')
		else:
			None

#Handler Error
def error(update, context):
	update.message.reply_text(f"Error! {logging.error}")

def main():
	#TOKEN
	Bot(TOKEN)
	dispatcher = updater.dispatcher
	#job_queue = updater.job_queue
	randintrval = random.uniform(30.0, 60.0)
	# add handlers for commands
	dispatcher.add_handler(CommandHandler("start", start))
	dispatcher.add_handler(CommandHandler("help", help))
	dispatcher.add_handler(CommandHandler("stop", stop))
	dispatcher.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), work_time))
	dispatcher.add_error_handler(error)
	#Start Asshole bot
	rerand
	updater.start_polling(poll_interval=randintrval, timeout=randintrval, drop_pending_updates=True)
	updater.idle()


if __name__ == '__main__':
	main()
