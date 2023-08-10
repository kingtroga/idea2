from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '680')
Config.write()

from kivymd.app import MDApp
from kaki.app import App
from kivy.lang import Builder
from kivy.factory import Factory
import os
from py.screens.manager_screen import ManagerScreen

# SCREENS/PYTHON
from py.screens.manager_screen import ManagerScreen
from py.screens.splash_screen_one import SplashScreenOne
from py.screens.splash_screen_two import SplashScreenTwo
from py.screens.onboarding import Onboarding
from py.screens.sign_up import SignUp
from py.screens.login_in import LoginIn
from py.screens.forgot_password import ForgotPassword
from py.screens.home import Home

# WIDGETS/PYTHON
from py.widgets.idealabel1 import IdeaLabel1
from py.widgets.avataritem import AvatarItem
from py.widgets.navbar import NavBar
from py.widgets.private_chats import PrivateChats
from py.widgets.group_chats import GroupChats
from py.widgets.announcements import Announcements
from py.widgets.settings_nav import SettingsNav
from py.widgets.topbar import TopBar



# SCREENS/KIVY
Builder.load_file("kv\screens\manager_screen.kv")
Builder.load_file("kv\screens\splash_screen_one.kv")
Builder.load_file("kv\screens\splash_screen_two.kv")
Builder.load_file("kv\screens\onboarding.kv")
Builder.load_file("kv\screens\sign_up.kv")
Builder.load_file("kv\screens\login_in.kv")
Builder.load_file("kv\screens\\forgot_password.kv")
Builder.load_file("kv\screens\\home.kv")


# WIDGETS/KIVY
Builder.load_file("kv\widgets\idealabel1.kv")
Builder.load_file("kv\widgets\\avataritem.kv")
Builder.load_file("kv\widgets\\navbar.kv")
Builder.load_file("kv\widgets\private_chats.kv")
Builder.load_file("kv\widgets\group_chats.kv")
Builder.load_file("kv\widgets\\announcements.kv")
Builder.load_file("kv\widgets\settings_nav.kv")
Builder.load_file("kv\widgets\\topbar.kv")






class iDeaApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Light"
        self.sm = ManagerScreen()
        return self.sm

""" class iDeaApp(App, MDApp):

    CLASSES = {
        "ManagerScreen": "py.screens.manager_screen",
        "SplashScreenOne": "py.screens.splash_screen_one",
        "IdeaLabel1": "py.widgets.idealabel1",
        "Header": "py.widgets.header",
        "BubbleItem": "py.widgets.bubbleitem",
        "ChatItem": "py.widgets.chatitem",
        "AvatarItem": "py.widgets.avataritem",
        "SmoothButton": "py.widgets.smoothbutton",
        #"CreateGroup": "py.screens.create_group",
        #"SearchScreen": "py.screens.search_screen",
    }

    KV_FILES = {
        os.path.join(os.getcwd(), "kv/screens/manager_screen.kv"),
        os.path.join(os.getcwd(), "kv/screens/splash_screen_one.kv"),
        #os.path.join(os.getcwd(), "kv/screens/create_group.kv"),
        os.path.join(os.getcwd(), "kv/widgets/idealabel1.kv"),
        os.path.join(os.getcwd(), "kv/widgets/header.kv"),
        os.path.join(os.getcwd(), "kv/widgets/bubbleitem.kv"),
        os.path.join(os.getcwd(), "kv/widgets/chatitem.kv"),
        os.path.join(os.getcwd(), "kv/widgets/avataritem.kv"),
        os.path.join(os.getcwd(), "kv/widgets/smoothbutton.kv"),
        #os.path.join(os.getcwd(), "kv/screens/search_screen.kv"),
    }

    AUTORELOADER_PATHS = [
        (".", {"recursive": True})
    ]
    def print_me(self):
        self.sm.current = "Screen1"

    def build_app(self):
        print("I'm reloading")
        self.sm = Factory.ManagerScreen()
        return self.sm """


if __name__ == '__main__':
    iDeaApp().run()