import telebot

from consts.login_const import *


class PostingBot():
    def __init__(self):
        self.bot = telebot.TeleBot(tg_token)
        self.channel = tg_channel

    def postMedia(self, image_set, text, url):
        #self.bot.send_photo(self.channel, image, text)
        self.bot.send_media_group(self.channel, [telebot.types.InputMediaPhoto(photo) for photo in image_set], text_msg)

