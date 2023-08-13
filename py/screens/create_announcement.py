from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from py.widgets.fake_private_chats import FakePrivateChats
from py.widgets.fake_group_chats import FakeGroupChats
from py.widgets.fake_announcements import FakeAnnouncements
from py.widgets.fake_settings import FakeSettings
from py.widgets.navbar2 import NavBar2

Builder.load_file("kv\widgets\\fake_private_chats.kv")
Builder.load_file("kv\widgets\\fake_group_chats.kv")
Builder.load_file("kv\widgets\\fake_announcements.kv")
Builder.load_file("kv\widgets\\fake_settings.kv")
Builder.load_file("kv\widgets\\navbar2.kv")

class CreateAnnouncement(Screen):
    def __init__(self, **kwargs):
        super(CreateAnnouncement, self).__init__(**kwargs)
        self.name = "Screen9"