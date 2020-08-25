import telebot

from consts.login_const import *


class PostingBot():
    def __init__(self):
        self.bot = telebot.TeleBot(tg_token)
        self.channel = tg_channel

    def postMedia(self, image_set, text, url, publicName):
        # self.bot.send_photo(self.channel, image, text)
        media_append = []
        for photo in image_set:
            media_append.append(telebot.types.InputMediaPhoto(photo))
        message = "Название паблика: "+publicName+" \nОригинальный пост: " + url
        if (text != ""):
            message += ' \n Текст поста: "' + text + '"'
        if publicName=="Как правильно воровать картинки":
            message=text
        media_append[0] = telebot.types.InputMediaPhoto(image_set[0], message)
        self.bot.send_media_group(self.channel, media_append)
    def postNews(self, text):
        self.bot.send_message(self.channel, text)
