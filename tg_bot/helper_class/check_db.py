from telegram.ext import Updater
from tg_bot.helper_class.default import update, dispatcher
from tg_bot.helper_class.APIs import connection
from functools import wraps
import pymongo
from pymongo import MongoClient


db = connection['aurora']
coll = db['dox']

def check_db(func):
    @wraps(func)
    def is_saved(bot, update, *args, **kwargs):
        user_id = update.message['from_user']['id']
        curs = coll.find({"user_id":user_id}, {"rate_limit":True, "_id":False})
        for item in curs:
            user = item.get("rate_limit", None)
            if user == 1000:
                pass
            else: 
                return func(bot, update, *args, **kwargs)
    return is_saved
