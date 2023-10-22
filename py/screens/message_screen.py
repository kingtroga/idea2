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

    def printIDS(self, app):
        self.app = app
        Clock.schedule_once(self.printid, 0.2)

    def printid(self, dt):
        self.ids['contactName'].text = self.app.contactFullName[:11]
        self.ids['messageBox'].handle_chatting()

    def closeCo(self):
        self.ids['messageBox'].counter = 1

