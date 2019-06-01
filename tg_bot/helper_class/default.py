from telegram.ext import Updater
from tg_bot.helper_class.APIs import TG_API
import pymongo

update = Updater(token=TG_API)
dispatcher = update.dispatcher