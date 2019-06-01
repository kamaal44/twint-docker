import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "are-lobsters-mermaids-for-scorpions"
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:343dfb3e@localhost/nure_timetable"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BOT_TOKEN = "795380923:AAFkZ7jXfkigItGJcfUw0svWQhB0fWcKI9w"
    TELEGRAM_API_LINK = "https://api.telegram.org/bot{}/{}"
    TIMETABLE_LINK = "http://cist.nure.ua/ias/app/tt/WEB_IAS_TT_GNR_RASP.GEN_GROUP_POTOK_RASP?ATypeDoc=3&Aid_group={}&Aid_potok=0&ADateStart={}&ADateEnd={}&AMultiWorkSheet=0"
    FILE_STORAGE_PATH = "./storage/"
