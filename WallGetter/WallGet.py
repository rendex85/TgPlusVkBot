import time

import requests
from vk_api import vk_api

from DataBase.PublicWorker import WorkWithWall
from TelegramTools.ChannelPost import *
from consts.login_const import *


class WallGetPost():
    def __init__(self):
        vk_session1 = vk_api.VkApi(phone, password)
        try:
            vk_session1.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
        self.vk = vk_session1.get_api()
        self.dbWall = WorkWithWall()

    def postMonitoring(self):
        while True:
            time.sleep(1)
            for public in self.dbWall.getPublics():
                postDict = self.vk.wall.get(owner_id="-" + str(public['public_id']))
                last_post = postDict['items'][0]
                if ('is_pinned' in postDict['items'][0]):
                    last_post = postDict['items'][1]
                    if (postDict['items'][0]['is_pinned'] == 0):
                        last_post = postDict['items'][0]
                #print(last_post)
                if public['last_post_id'] != last_post['id']:
                    postTg = PostingBot()
                    image_set = []
                    postText = last_post['text']
                    if 'attachments' in last_post:
                        for att in last_post['attachments']:
                            if att['type'] == 'photo':
                                photo_url = att['photo']['sizes'][-1]['url']
                                session = requests.Session()
                                img = session.get(photo_url, stream=True)
                                image_set.append(img.raw)
                        if len(image_set)>0:
                            postUrl="vk.com/wall"+"-"+str(public['public_id'])+"_"+str(last_post['id'])
                            postTg.postMedia(image_set, postText, postUrl)
                            time.sleep(1)

                    self.dbWall.addLastPost(public['public_id'], int(last_post['id']))
