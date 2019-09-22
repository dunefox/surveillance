import telegram as tg
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import config as cfg
import funcs as fnc 
import logging  

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token=cfg.token, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', fnc.start)
caps_handler = CommandHandler('caps', fnc.caps)
echo_handler = MessageHandler(Filters.text, fnc.echo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caps_handler)

bot = tg.Bot(cfg.token)

print(bot.get_me())


updater.start_polling()
updater.idle()

