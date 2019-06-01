from telegram.ext import CommandHandler, RegexHandler
from telegram.error import BadRequest
from tg_bot.helper_class.APIs import EMAIL_API
from tg_bot.helper_class.APIs import connection
from tg_bot.helper_class.default import update, dispatcher
from tg_bot.helper_class.rate_limit import rate_limit
from telegram import ParseMode
from fullcontact import FullContact
import pymongo
import json
import re


db = connection['aurora']
coll = db['dox']

@rate_limit
def full(bot, update):
    fc = FullContact(EMAIL_API)
    u_mail = update.message.text
    r = fc.person(email=u_mail)
    js = r.json()
    api_status = js['status']

    if api_status == 403:
        bot.send_message(chat_id=update.message.chat_id, text="Please try again later. If the problem persists please contact [my creator](https://t.me/snoopdoggystyledogg)",
                parse_mode=ParseMode.MARKDOWN)
    else:
        user_id = update.message['from_user']['id']
        curs = coll.find({"user_id":user_id}, {"rate_limit":True, "_id":False})
        for item in curs:
            get_limit = str(item.get("rate_limit", None))
            sum_limit = 1
            for add in get_limit:
                add_limit = sum_limit + int(add)
                coll.update_one(
                {'user_id': user_id},
                {"$set": {

                   'rate_limit': add_limit
                }
                }
                )
        search_social = ['github', 'twitter','facebook', 'linkedin']
        urls = {dct['type']: dct['url'] for dct in js.get('socialProfiles', []) if dct['type'] in search_social}
        search_bio = ['twitter']
        bios = {dct['type']: dct['bio'] for dct in js.get('socialProfiles', []) if dct['type'] in search_bio}
        github_link = urls.get('github', None)
        twitter_link = urls.get('twitter', None)
        fb_link = urls.get('facebook', None)
        linkedin = urls.get('linkedin', None)
        twi_bio = bios.get('twitter')

        try:
            demog = js.get('demographics', None)
            locd = demog.get('locationDeduced', None)
            address = locd.get('normalizedLocation', None)
            age = demog.get('age', None)
        except AttributeError:
            address = 'None'
            age = 'None'
        try:
            contact_info = js.get('contactInfo', None)
            full_name = contact_info = contact_info.get('fullName', None)
        except AttributeError:
            full_name = 'None'
        try:
            org_name = js['organizations'][0]['name']
            org_title = js['organizations'][0]['title']
            job = "{} at {}".format(org_title, org_name)
        except KeyError:
            job ='None'
        try:
            photo = js['photos'][0]['url']
        except KeyError:
            photo = " "



        CAT = """
        Info About: {}

        Name: {}

        Age: {}

        Address: {}

        Current Job: {}

        Bio: {}

        Github: {}

        Twitter: {}

        Facebook: {}

        Linkedin: {}

        """.format(u_mail, full_name, age, address, job, twi_bio, github_link, twitter_link, fb_link, linkedin)
       
        REPLY = re.sub(r'\bNone\b', 'None Found', CAT)
        left_headers = r.headers['x-rate-limit-remaining']
        try:
            bot.sendPhoto(chat_id=update.message.chat_id, photo=photo)
        except BadRequest:
            pass
        bot.send_message(chat_id=update.message.chat_id, text=REPLY, disable_web_page_preview=True)
 
find_handler = RegexHandler(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]", full)
               
dispatcher.add_handler(find_handler)
