import threading

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from DataBase.PublicWorker import *
from WallGetter.WallGet import *
import logging
logging.basicConfig(filename='app.log', filemode='w')
vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, public)
vk = vk_session.get_api()


def main():
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            peer = event.obj.peer_id
            from_id = event.obj.from_id

            if (event.obj.text.lower().find('!пабадд') != (-1)) and (from_id == 232282950 or from_id == 204181697):
                publicPost = PublicDbWorker(peer, event.obj.text, vk)
                publicPost.addPublic()

            if (event.obj.text.lower().find('!пабдел') != (-1)) and (from_id == 232282950 or from_id == 204181697):
                publicPost = PublicDbWorker(peer, event.obj.text, vk)
                publicPost.removePublic()
            if event.obj.text.lower().find('!список') != (-1):
                wallWorker = WorkWithWall()
                vk.messages.send(peer_id=peer, random_id=0, message=wallWorker.publicList())


if __name__ == '__main__':

    wall = WallGetPost()
    poster = threading.Thread(target=wall.postMonitoring)
    poster.start()
    while True:
        try:
            main()
        except Exception:
            logging.error("Fatal error in main loop", exc_info=True)
