from uuid import uuid4

from telebot.types import *
from fuzzywuzzy import utils as fuzzy_utils


SHRUG = '¯\_(ツ)_/¯'

def lines_processor(item):
    if isinstance(item, str):
        pass
    else:
        item = item.name + ' ' + item.tags
    return fuzzy_utils.full_process(item)

def uuid():
    return uuid4().hex

def article(title: str, content: str = SHRUG, **kwargs):
    message_content = InputTextMessageContent(content, parse_mode='html')
    return InlineQueryResultArticle(uuid(), title, message_content, **kwargs)

