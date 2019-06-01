from telegram.ext import CommandHandler, RegexHandler, MessageHandler, Filters
from tg_bot.helper_class.default import update, dispatcher
from tg_bot.helper_class.check_db import check_db
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers.phonenumberutil import region_code_for_country_code
from phonenumbers.phonenumberutil import region_code_for_number
from phonenumbers.phonenumberutil import NumberParseException
import json
import re

@check_db
def phone_number(bot, update):
    try:
        nr = update.message.text
        pn = phonenumbers.parse(update.message.text, None)
        c = carrier.name_for_number(pn, "en")
        c_code = region_code_for_country_code(pn.country_code)
        geo = geocoder.description_for_number(pn, "en")
        val = phonenumbers.is_valid_number(pn)
        
        if val == False:
            bot.send_message(chat_id=update.message.chat_id, text="{} is not a valid number. Please check the phone number and try again".format(nr))
        else:

            REPLY = """
            Info about {}:
            \n Country Name: {}
            \n Country Code: {}
            \n Carrier: {}
            """.format(nr, geo, c_code, c)
            bot.send_message(chat_id=update.message.chat_id, text=REPLY, disable_web_page_preview=True)
    except NumberParseException as e:
        bot.send_message(chat_id=update.message.chat_id, text="Missing or invalid default region.")


phone_handler = RegexHandler(r'(^[+0-9]{1,3})*([0-9]{10,11}$)', phone_number)
               
dispatcher.add_handler(phone_handler)

