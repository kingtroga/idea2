
from kivymd.app import MDApp
from py.screens.testScreen import TestScreen
from py.widgets.navbar import NavBar
from py.widgets.fake_private_chats import FakePrivateChats
from py.widgets.fake_group_chats import FakeGroupChats
from py.widgets.fake_announcements import FakeAnnouncements
from py.widgets.fake_settings import FakeSettings
from kivy.lang import Builder

Builder.load_file("screen.kv")
Builder.load_file("kv\widgets\\navbar.kv")
Builder.load_file("kv\widgets\\fake_private_chats.kv")
Builder.load_file("kv\widgets\\fake_group_chats.kv")
Builder.load_file("kv\widgets\\fake_announcements.kv")
Builder.load_file("kv\widgets\\fake_settings.kv")


class TestApp(MDApp):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.ACCESS_TOKEN = "19010301043"
        
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Light"
        return TestScreen()
    
if __name__ == "__main__":
    TestApp().run()