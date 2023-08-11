
from kivymd.app import MDApp
from py.screens.testScreen import TestScreen
from py.screens.create_group import CreateGroup
from py.widgets.navbar import NavBar
from py.widgets.private_chats import PrivateChats
from py.widgets.group_chats import GroupChats
from py.widgets.announcements import Announcements
from py.widgets.settings_nav import SettingsNav
from py.widgets.topbar import TopBar
#from py.widgets.imagebutton import ImageButton
from kivy.lang import Builder

Builder.load_file("screen.kv")
Builder.load_file("kv\screens\create_group.kv")
Builder.load_file("kv\widgets\\navbar.kv")
Builder.load_file("kv\widgets\private_chats.kv")
Builder.load_file("kv\widgets\group_chats.kv")
Builder.load_file("kv\widgets\\announcements.kv")
Builder.load_file("kv\widgets\settings_nav.kv")
Builder.load_file("kv\widgets\\topbar.kv")
#Builder.load_file("kv\widgets\imagebutton.kv")

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