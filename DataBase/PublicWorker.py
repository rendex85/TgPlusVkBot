from DataBase.Models import *


class PublicDbWorker():
    def __init__(self, peer_id, msg, vk):
        self.vk = vk
        self.peer_id = peer_id
        self.msg = msg
        self.public = ""
        strtssyl = self.msg.find("vk.com/")
        if strtssyl != -1:
            endssyl = self.msg[strtssyl + len("vk.com/"):].find(' ')
            if endssyl == -1:
                self.public = self.msg[strtssyl + len("vk.com/"):]
            else:
                self.public = self.msg[strtssyl + len("vk.com/"): endssyl]
        public_info = vk.groups.getById(group_id=self.public, fields='counters')
        self.public = public_info[0]['id']
        self.public_name = public_info[0]['name']

    def addPublic(self):
        Publics.insert(public_id=int(self.public), public_url=self.msg[self.msg.find("vk.com/"):],
                       public_name=self.public_name).execute()
        self.vk.messages.send(peer_id=self.peer_id, random_id=0,
                              message="Паблик " + self.msg[self.msg.find("vk.com/"):] + " успешно добавлен в пулл")
        closeConnect()

    def removePublic(self):
        delPublic = Publics.get(Publics.public_id == int(self.public))
        publicName = delPublic.public_url
        delPublic.delete_instance()
        self.vk.messages.send(peer_id=self.peer_id, random_id=0,
                              message="Паблик " + publicName + " успешно убран из пулла")
        closeConnect()


class WorkWithWall():
    def getPublics(self):
        publics = []
        query = Publics.select(Publics.public_id, Publics.last_post_id, Publics.public_name, Publics.public_url)
        result = query.dicts().execute()
        for row in result:
            publics.append(row)
        closeConnect()
        return publics

    def addLastPost(self, publicId, postId):
        Publics.update(last_post_id=postId).where(Publics.public_id == publicId).execute()
        closeConnect()
    def publicList(self):
        publicString="Список пабликов: \n"
        for public in self.getPublics():
            publicString+=str(public['public_name']) +": "+str(public['public_url'])+"\n"
        return publicString
