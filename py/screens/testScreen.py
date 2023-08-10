from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from py.widgets.private_chats import PrivateChats

class TestScreen(MDScreen):
    def __init__(self, **kwargs):
        super(TestScreen, self).__init__(**kwargs)
        #Clock.schedule_once(self.work, 1)
    

        
