from uuid import uuid4

from telebot.types import *

from .. import bot
from .voicelines import bot


help_msg = '''Ok, looks like I've forgot to add something.
Please, say what you did to @hatkidchan'''


@bot.inline_handler(func=lambda q: True)
def bot_inline_fb(q):
    try:
        bot.answer_inline_query(q.id, [
            InlineQueryResultArticle(
                uuid4().hex,
                'How did you got here?',
                InputTextMessageContent(help_msg))
        ], cache_time=0, is_personal=True)
    except:
        pass

