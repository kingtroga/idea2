from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '680')
Config.write()

from kivymd.app import MDApp
from kivy.lang import Builder


# SCREENS/PYTHON
from py.screens.manager_screen import ManagerScreen
from py.screens.splash_screen_one import SplashScreenOne
from py.screens.splash_screen_two import SplashScreenTwo
from py.screens.onboarding import Onboarding
from py.screens.sign_up import SignUp
from py.screens.login_in import LoginIn
from py.screens.forgot_password import ForgotPassword
from py.screens.home import Home
from py.screens.create_group import CreateGroup

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
Builder.load_file("kv\screens\create_group.kv")


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

    def on_stop(self):
        print("Goodbye, World!")


if __name__ == '__main__':
    iDeaApp().run()