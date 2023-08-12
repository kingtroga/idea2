from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from py.widgets.fake_private_chats import FakePrivateChats
from py.widgets.fake_group_chats import FakeGroupChats
from py.widgets.fake_announcements import FakeAnnouncements
from py.widgets.fake_settings import FakeSettings

Builder.load_file("kv\widgets\\fake_private_chats.kv")
Builder.load_file("kv\widgets\\fake_group_chats.kv")
Builder.load_file("kv\widgets\\fake_announcements.kv")
Builder.load_file("kv\widgets\\fake_settings.kv")

class CreateAnnouncement(Screen):
    def __init__(self, **kwargs):
        super(CreateAnnouncement, self).__init__(**kwargs)
        self.name = "Screen9"