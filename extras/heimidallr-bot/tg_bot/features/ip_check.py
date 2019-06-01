from telegram.ext import CommandHandler, RegexHandler
from tg_bot.helper_class.default import update, dispatcher
from tg_bot.helper_class.check_db import check_db
from tg_bot.helper_class.APIs import IP_API
from telegram import Location
from telegram import Update
import requests
import json

@check_db
def ip_tracker(bot, update):
    ip = update.message.text
    API = {"access_key": IP_API}
    url = 'http://api.ipstack.com/' + ip
    request = requests.post(url, params=API).text
    r = json.loads(request)

    continent_code = r.get("continent_code", None)
    continent_name = r.get("continent_name", None)
    country_code = r.get("country_code", None)
    country_name = r.get("country_name", None)
    region_code = r.get("region_code", None)
    region_name = r.get("region_name", None)
    city_name = r.get("city", None)
    latitude = r.get("latitude", None)
    longitude = r.get("longitude", None)
    country_flag = r['location'].get("country_flag_emoji", None)


    REPLY = """
    Info about: {}

    Continent Code: {}

    Continent Name: {}

    Country Code: {}

    Country Name: {}

    Contry Flag: {}

    Region Code: {}

    Region Name: {}

    City: {}

    Latitude: {}

    Longitude: {}

    """.format(ip, continent_code, continent_name, country_code, country_name, country_flag, region_code, region_name, city_name, latitude, longitude)
    bot.send_message(chat_id=update.message.chat_id, text=REPLY)

    if latitude is not None and longitude is not None:
        location =  Location(longitude, latitude)
        bot.send_location(chat_id=update.effective_chat.id, location=location)


dispatcher.add_handler(RegexHandler(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip_tracker))