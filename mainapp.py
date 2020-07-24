#!/usr/bin/env python3
from telebot import TeleBot
from os import environ

bot = TeleBot(environ.get('BOT_TOKEN'))
from handlers import bot

