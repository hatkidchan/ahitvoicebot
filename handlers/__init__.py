from telebot.types import *

from mainapp import bot
from .inline import bot


hewwo_message = '''Oh hi there!
I can send voice messages with sounds from A Hat in Time by GfB!
Just type somewhere @ahitvoicebot and check it out!

By the way, I've made by @hatkidchan, feel free to say hewwo :)

---
О, привет!
Я могу отправлять голосовые сообщения с репликами из A Hat in Time от Gears for Breakfast!
Просто напиши где угодно @ahitvoicebot и попробуй сам!

Меня сделал @hatkidchan, если хотите помочь держать бота живым или просто поговорить - всегда рад :)
'''


TRY_KBD = InlineKeyboardMarkup()
TRY_KBD.row_width = 1
TRY_KBD.add(InlineKeyboardButton('Check it out', switch_inline_query=' '))


@bot.message_handler(commands=['start', 'help'])
def bot_hewoo(msg):
    bot.send_message(msg.chat.id, hewwo_message,
                     parse_mode='html', reply_markup=TRY_KBD)

