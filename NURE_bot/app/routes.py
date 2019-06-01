from app import app, bot, db
from app.models import User
from flask import request

@bot.message_handler(commands=['start'])
def start(message):
    db.session.add(User(message.from_user.username))
    bot.send_message(message.chat.id, "Спасибо, что решили воспользоваться именно этим расписанием!")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@app.route("/795380923:AAFkZ7jXfkigItGJcfUw0svWQhB0fWcKI9w", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://nure-timetable.herokuapp.com/795380923:AAFkZ7jXfkigItGJcfUw0svWQhB0fWcKI9w")
    return "!", 200
    
