import telebot

from consts.login_const import *


class PostingBot():
    def __init__(self):
        self.bot = telebot.TeleBot(tg_token)
        self.channel = tg_channel

    def postMedia(self, image, text):
        self.bot.send_photo(self.channel, image, text)
