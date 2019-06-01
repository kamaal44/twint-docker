from telegram.ext import Updater
from tg_bot.helper_class.default import update, dispatcher
from tg_bot.helper_class.APIs import connection
from functools import wraps
import pymongo
from pymongo import MongoClient

db = connection['aurora']
coll = db['dox']

def rate_limit(func):
    @wraps(func)
    def is_limited(bot, update, *args, **kwargs):
        user_id = update.message['from_user']['id']
        curs = coll.find({"user_id":user_id}, {"rate_limit":True, "_id":False})
        for item in curs:
            limit_count = item.get("rate_limit", None)
            if limit_count == 10:
                bot.send_message(chat_id=update.message.chat_id, text='You have hit the limit of searches for this beta. Wait for the full release.')
                pass
            else: 
                return func(bot, update, *args, **kwargs)
    return is_limited
