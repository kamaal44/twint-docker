
from telegram.ext import CommandHandler, MessageHandler
from telegram.ext import Filters
from telegram.error import BadRequest
from tg_bot.helper_class.default import update, dispatcher
from tg_bot.helper_class.check_db import check_db

import re
import whois.whois as pywhois
from whois.parser import PywhoisError
from socket import gaierror

@check_db
def whois(bot, update):
    try:
        url = update.message.text
        w = pywhois(url)
        domain_name = w.get('domain_name', None)
        registrar = w.get('registrar', None)
        whois_server = w.get('whois_server', None)
        creation_date = w.get('creation_date', None)
        updated_date = w.get('updated_date', None)
        expiration_date = w.get('expiration_date', None)
        get_servers = w.get('name_servers', None)
        name_servers =', '.join(get_servers)
        get_emails = w.get('emails', None)
        emails = ', '.join(get_emails)
        organisation = w.get('org', None)
        address = w.get('address', None)
        city = w.get('city', None)
        state = w.get('state', None)
        zipcode = w.get('zipcode', None)
        country = w.get('country', None)

        REPLY = """
        Info about: {}:

        Registrar: {}

        Whois Server: {}

        Creation Date {}

        Updated Date: {}

        Expiration Date: {}

        Servers Names: {}

        Emails: {}

        Organisation: {}

        Address: {}

        City: {}

        State: {}

        ZipCode: {}

        Country: {}

        """.format(domain_name, registrar, whois_server, creation_date, updated_date, expiration_date, 
                                name_servers, emails, organisation, address, city, state, zipcode, country)
        bot.send_message(chat_id=update.message.chat_id, text=REPLY)
    except gaierror:
        bot.send_message(chat_id=update.message.chat_id, text='Name or service not known. The Registry database contains ONLY .COM, .NET, .EDU domains and Registrars.')
    except PywhoisError:
        bot.send_message(chat_id=update.message.chat_id, text='No match for {}. The Registry database contains ONLY .COM, .NET, .EDU domains and Registrars.'.format(url))

    
dispatcher.add_handler(MessageHandler(Filters.entity('url'), whois))