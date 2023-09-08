from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivy.clock import Clock
from py.widgets.chatitem import ChatItem
from kivy.properties import StringProperty, NumericProperty
from kivy.metrics import dp
from kivy.utils import get_color_from_hex

class SettingsNav(MDBottomNavigationItem):
    def __init__(self, **kwargs):
        super(SettingsNav, self).__init__(**kwargs)
        #Clock.schedule_once(self.show_settings, 0.5)

    def show_settings(self, dt):
        #print("I'm a boy")
        # USER PROFILE
        self.ids['aBox'].add_widget(
            ChatItem(
            #icon2 = "key-outline",
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
            font_fam1= "fonts/ARIALMTMEDIUM.TTF",
            ))
        
        # PRIVACY
        self.ids['aBox'].add_widget(
            ChatItem(
            icon2 = "key-outline",
            #avatar='images/4.jpg',
            uppertext='Account',
            lowertext='Privacy, security, change number',
            timeline="",
            icon="",
            #icon_size=dp(45),
            is_bold=False,
            text_icon_dis= 77,
            uppertextY= 4,
            lowertextY= 20,
            pos= (self.ids['settingsLayout'].width - self.ids['settingsLayout'].width +30 , self.ids['settingsLayout'].height -210),
            back_color= get_color_from_hex("FFFFFF"),
            font_fam1= "fonts/arialmt.TTF",
            uppertext_size = dp(18),
            lowertext_size = dp(15),
            ))
        
        # CHAT
        self.ids['aBox'].add_widget(
            ChatItem(
            icon2 = "message-processing-outline",
            #avatar='images/4.jpg',
            uppertext='Chat',
            lowertext='Chat history,theme,wallpapers',
            timeline="",
            icon="",
            #icon_size=dp(45),
            is_bold=False,
            text_icon_dis= 77,
            uppertextY= 4,
            lowertextY= 20,
            pos= (self.ids['settingsLayout'].width - self.ids['settingsLayout'].width +30 , self.ids['settingsLayout'].height -290),
            back_color= get_color_from_hex("FFFFFF"),
            font_fam1= "fonts/arialmt.TTF",
            uppertext_size = dp(18),
            lowertext_size = dp(15),
            ))
        
        # NOTIFICATIONS

        self.ids['aBox'].add_widget(
            ChatItem(
            icon2 = "bell-outline",
            #avatar='images/4.jpg',
            uppertext='Notifications',
            lowertext='Messages, groups and others',
            timeline="",
            icon="",
            #icon_size=dp(45),
            is_bold=False,
            text_icon_dis= 77,
            uppertextY= 4,
            lowertextY= 20,
            pos= (self.ids['settingsLayout'].width - self.ids['settingsLayout'].width +30 , self.ids['settingsLayout'].height -380),
            back_color= get_color_from_hex("FFFFFF"),
            font_fam1= "fonts/arialmt.TTF",
            uppertext_size = dp(18),
            lowertext_size = dp(15),
            ))
        
       
        
        # HELP
        self.ids['aBox'].add_widget(
            ChatItem(
            icon2 = "help-circle-outline",
            #avatar='images/4.jpg',
            uppertext='Help',
            lowertext='Help center,contact us,privacy policy',
            timeline="",
            icon="",
            #icon_size=dp(45),
            is_bold=False,
            text_icon_dis= 77,
            uppertextY= 4,
            lowertextY= 20,
            pos= (self.ids['settingsLayout'].width - self.ids['settingsLayout'].width +30 , self.ids['settingsLayout'].height - 470),
            back_color= get_color_from_hex("FFFFFF"),
            font_fam1= "fonts/arialmt.TTF",
            uppertext_size = dp(18),
            lowertext_size = dp(15),
            ))
        
        # STORAGE AND DATA
        self.ids['aBox'].add_widget(
            ChatItem(
            icon2 = "swap-vertical",
            #avatar='images/4.jpg',
            uppertext='Storage and data',
            lowertext='Network usage, storage usage',
            timeline="",
            icon="",
            #icon_size=dp(45),
            is_bold=False,
            text_icon_dis= 77,
            uppertextY= 4,
            lowertextY= 20,
            pos= (self.ids['settingsLayout'].width - self.ids['settingsLayout'].width +30 , self.ids['settingsLayout'].height - 560),
            back_color= get_color_from_hex("FFFFFF"),
            font_fam1= "fonts/arialmt.TTF",
            uppertext_size = dp(18),
            lowertext_size = dp(15),
            ))
        
        # INVITES
        self.ids['aBox'].add_widget(
            ChatItem(
            icon2 = "account-multiple-outline",
            #avatar='images/4.jpg',
            uppertext='Invite a friend',
            lowertext='',
            timeline="",
            icon="",
            #icon_size=dp(45),
            is_bold=False,
            text_icon_dis= 77,
            uppertextY= -7.4,
            lowertextY= 20,
            pos= (self.ids['settingsLayout'].width - self.ids['settingsLayout'].width +30 , self.ids['settingsLayout'].height - 640),
            back_color= get_color_from_hex("FFFFFF"),
            font_fam1= "fonts/arialmt.TTF",
            uppertext_size = dp(18),
            lowertext_size = dp(15),
            ))
                





        





        





        




