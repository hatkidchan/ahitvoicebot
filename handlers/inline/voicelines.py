from os import environ
from json import load
from typing import *

from fuzzywuzzy import process as fuzzy_process
from telebot import TeleBot
from telebot.types import *

from . import bot
from .utils import *
from .voicestorage import *


INLINE_RESULT_EMPTY_SET = article('Nothing found')
InlineResult = Union[InlineQueryResultArticle, InlineQueryResultVoice]


cache = {}
cache['global'] = VoicePack('glob', 'Global search', '', [])
cache.update({
    k: VoicePack.de_json(v)
    for k, v
    in load(open(environ.get('LIST_PATH'), 'r')).items()
})


class PackHandler:
    def __init__(self, bot: TeleBot, data: VoicePack):
        self.bot = bot
        self.cache = data.lines
        self.name = data.name
        self.prefix = data.prefix
        
    def answer_inline(self,
                      query_id: str,
                      results: List[InlineResult],
                      next_offset: Optional[int] = None) -> None:
        if not results:
            results = [INLINE_RESULT_EMPTY_SET]
        try:
            self.bot.answer_inline_query(query_id, results,
                                         next_offset=next_offset)
        except:
            pass

    def handle_listing(self, query: InlineQuery) -> None:
        results = []
        
        start = int(query.offset or 0)
        data = self.cache

        for line in data[start : start + 30]:
            url, name, _ = line
            if self.prefix == 'global':
                name = f'{line.parent_pack.prefix} | {name}'
            results.append(InlineQueryResultVoice(uuid(), url, name))
            
        next_offset = start + 30 if len(data[start:]) >= 30 else None
        self.answer_inline(query.id, results, next_offset=next_offset)

    def handle_search(self, query: InlineQuery) -> None:
        results = []
        
        start = int(query.offset or 0)
        data = self.cache
        search = query.query[len(self.prefix) + 1 : ]

        values = fuzzy_process.extract(search, data, processor=lines_processor)
        for line, prob in values[start : start + 30]:
            url, name, _ = line
            if prob < 30:
                break
            if self.prefix == 'global':
                name = f'{line.parent_pack.prefix} | {name}'
            display = f'{prob}% {name}'
            results.append(InlineQueryResultVoice(uuid(), url, display))

        next_offset = start + 30 if len(data[start:]) >= 30 else None
        self.answer_inline(query.id, results, next_offset=next_offset)
    
    def test_listing(self, query: InlineQuery) -> bool:
        return query.query.strip() == self.prefix
    
    def test_search(self, query: InlineQuery) -> bool:
        return query.query.strip().startswith(self.prefix + ' ')


for k, pack in cache.items():
    handler = PackHandler(bot, pack)
    bot.inline_handler(func=handler.test_listing)(handler.handle_listing)
    bot.inline_handler(func=handler.test_search)(handler.handle_search)
    if k != 'global':
        cache['global'].lines += pack.lines


@bot.inline_handler(func=lambda q: q.query.strip() == '')
def bot_list_packs(query):
    results = []
    start = int(query.offset or 0)

    for k, pack in cache.items():
        kbd = InlineKeyboardMarkup()
        kbd.row_width = 1
        btn = InlineKeyboardButton('Check it out',
                                   switch_inline_query_current_chat=pack.prefix)
        kbd.add(btn)
        results.append(article(title=pack.name,
                               content=repr(pack),
                               description=str(pack),
                               reply_markup=kbd))

    next_offset = start + 30 if len(results) > start + 30 else None
    try:
        bot.answer_inline_query(query.id, results[:30], next_offset=next_offset)
    except:
        pass
