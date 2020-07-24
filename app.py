import json
from os import environ

import flask
import telebot

from mainapp import bot


WEBHOOK_HOST = environ.get('WEBHOOK_HOST')
WEBHOOK_PATH = environ.get('WEBHOOK_PATH')


app = flask.Flask(__name__)


@app.route(WEBHOOK_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8101', debug=False)

