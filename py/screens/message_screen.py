from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock
from PIL import Image
from py.widgets.imagebutton import ImageButton

from py.widgets.messagebox import MessageBox
Builder.load_file("kv/widgets/messagebox.kv")

class MessageScreen(Screen):
    def __init__(self, **kwargs):
        super(MessageScreen, self).__init__(**kwargs)
        self.name = "Screen10"
        self.appStart = True

        self.user_list = {"1" : "image_1", "2" : "image_2", "3" : "image_3", 
                "4" : "image_4", "5" : "image_5", "6" : "image_6", }
        self.uppertext_list = {"1": "Dr. Balogun", "2": "300L Computer Sc..", 
                "3": "Abraham John", "4": "Shalom", 
                "5": "19010301024", "6":"Angel Dayna"}

        self.lowertext_list = {"1": "I haven't seen your assign...", "2":"There will be CSC 307 class...",
                "3": "Hey! Can you join the meeting?", "4": "How are you today?",
                "5": "Have a good day🌸", "6": "How are you today?"}

        self.timeline_list = {"1": "2 min ago", "2": "2 min ago", "3": "2 min ago",
                "4": "5 min ago", "5": "yesterday", "6": "2 min ago"}

        self.icon_list = {"1": "numeric-3-circle", "2": "numeric-4-circle", "3":"",
            "4":"", "5":"", "6":""}
        #################################################

    def show_storys_and_chats(self, dt=None):
        if self.appStart:
            for i in self.user_list:
                self.ids['rv'].data.append({
                            'avatar' : f'images\{i}.jpg',
                            "uppertext": self.uppertext_list[i],
                            "lowertext": self.lowertext_list[i],
                            "timeline": self.timeline_list[i],
                            "icon": self.icon_list[i]
                        })
            self.appStart = False

    def printIDS(self):
        Clock.schedule_once(self.printid, 2)

    def printid(self, dt):
        print(self.ids)
