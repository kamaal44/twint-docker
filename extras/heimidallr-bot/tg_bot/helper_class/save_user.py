from telegram.ext import CommandHandler, Filters, MessageHandler
from telegram.error import BadRequest
from telegram.ext.dispatcher import run_async
from tg_bot.helper_class.default import update, dispatcher
from tg_bot.helper_class.APIs import connection
from telegram import ParseMode
from typing import Optional, List
from telegram.utils.helpers import escape_markdown

import json
import pymongo
from pymongo import MongoClient
import re
import math


db = connection['aurora']
coll = db['dox']

@run_async
def save(bot, update):
    chat_id = update.message['chat']['id']
    user_id = update.message['from_user']['id']
    user_name = update.message['from_user']['username']
    try:
        cursor = coll.aggregate([{"$group": {"_id": None, "my_list": {"$push": "$user_id"}}}])
        my_list = next(cursor)["my_list"]
        if user_id in my_list:

            bot.send_message(chat_id=update.message.chat_id, text='Thanks for using my bot.\nYou can see what I can do with /help. \nFind how to donate with /donate/ \nFor any problems contact @snoopdoggystyledogg')
            pass
        else:
            doc = {
            'type': 'user',
            'user_id': user_id,
            'user_name': user_name,
            'rate_limit': 0,
	        }
            coll.insert_one(doc).inserted_id
            bot.send_message(chat_id=update.message.chat_id, text='Thanks for using my bot.\nYou can see what I can do with /help. \nFind how to donate with /donate. \nFor any problems contact @snoopdoggystyledogg')
    except StopIteration:

        doc = {
        'type': 'user',
        'user_id': user_id,
        'user_name': user_name,
        'rate_limit': 0,
	    }
        coll.insert_one(doc).inserted_id

        bot.send_message(chat_id=update.message.chat_id, text='Thanks for using my bot.\nYou can see what I can do with /help. \nFind how to donate with /donate. \nFor any problems contact @snoopdoggystyledogg')


yes_handler = CommandHandler('yes', save)
dispatcher.add_handler(yes_handler)