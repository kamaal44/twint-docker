from telegram.ext import CommandHandler
from tg_bot.helper_class.default import update, dispatcher
from tg_bot.helper_class import save_user
from tg_bot.features import *
from tg_bot.helper_class.APIs import connection
import logging
import pymongo


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(bot, update):
    REPLY = """

    
    - Hi! I'm Heimdall!. "My eyes, they see everything".
    
    \nMy purpose is to help you feel more secure around telegram. \nUse this on your own risk.
    \n- I'm not responsible for any of the users that may use this bot agaist you.
    \n- Some commands have a request limit x/month
    \n- The request limit will reset on 9th every month for every user that has more than 15 requests.
    \nReply with /yes if you agree with all of these terms. 

    

"""
    bot.send_message(chat_id=update.message.chat_id, text=REPLY)

def help(bot, update):

    REPLY = """

    Hi, I'm Heimdall. "My eyes, they see everything":

    - * Type an email and get all the info I can find about his owner.
    - Type a phone number and I can get you his location
    - Type an IP and I can send anything I can find about it.
    - Type a web adress and get the info about his domain

    \nI Command noted with * have a request limit. Find about ratelimit with /limit
    \nThe bot is curently running on a free heroku plan. Help me upgrade to another VPS with /donate

    \nFor any problems contact @snoopdoggystyledogg


    """



    bot.send_message(chat_id=update.message.chat_id, text=REPLY)


def donate(bot, update):

    REPLY = """

    Hi! This bot is curently running on a free heroku server and sometimes it might feel slow
    \nHelp me with a donation at https://www.paypal.me/marcelalexandrunitan.

    \nDonate and help me upgrade to another VPS

    """

    bot.send_message(chat_id=update.message.chat_id, text=REPLY)
    
def limit(bot, update):
    
    REPLY = "For this beta you'll be limited to 10 requests only for email searches.\nAfter release will be limited to 30"
    bot.send_message(chat_id=update.message.chat_id, text=REPLY)

def count(bot, update):
    db = connection['aurora']connect
    coll = db['dox']
    usrs = coll.count()
    bot.send_message(chat_id=update.message.chat_id, text="Users: {}".format(usrs))

def main():
    update.start_polling()




dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('donate', donate))
dispatcher.add_handler(CommandHandler('limit', limit))
dispatcher.add_handler(CommandHandler('stats', count))

if __name__ == '__main__':
    main()
