import time

from vk_api import vk_api

from DataBase.PublicWorker import WorkWithWall
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
                postDict=self.vk.wall.get(owner_id="-" + str(public['public_id']))
                last_post= postDict['items'][0]['id']
                if ('is_pinned' in postDict['items'][0]):
                    last_post = postDict['items'][1]['id']
                    if (postDict['items'][0]['is_pinned']==0):
                        last_post = postDict['items'][0]['id']
                if public['last_post_id'] != last_post:
                    self.dbWall.addLastPost(public['public_id'], int(last_post))
                    print(last_post)
