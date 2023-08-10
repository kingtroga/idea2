from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivy.clock import Clock
from py.widgets.chatitem import ChatItem
from kivy.properties import StringProperty, NumericProperty
from kivy.metrics import dp
from kivy.utils import get_color_from_hex

class SettingsNav(MDBottomNavigationItem):
    def __init__(self, **kwargs):
        super(SettingsNav, self).__init__(**kwargs)
        Clock.schedule_once(self.show_settings, 0.5)

    def show_settings(self, dt):
        print("I'm a boy")
        self.ids['aBox'].add_widget(
            ChatItem(
            avatar='images/4.jpg',
            uppertext='Janet Doe',
            lowertext='Who am I?',
            timeline="",
            icon="",
            icon_size=dp(45),
            is_bold=True,
            text_icon_dis= 94,
            uppertextY= 4,
            lowertextY= 20,
            pos= (self.ids['settingsLayout'].width - self.ids['settingsLayout'].width + 20 , self.ids['settingsLayout'].height -110),
            back_color= get_color_from_hex("FFFFFF"),
            font_fam1= "fonts/ARIALMTMEDIUM.TTF"
            ))

