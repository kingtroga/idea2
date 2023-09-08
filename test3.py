from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem

from kivymd.uix.fitimage import FitImage
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.utils import get_color_from_hex



 

Builder.load_string(
'''
#:import images_path kivymd.images_path


<CustomOneLineIconListItem>

    IconLeftWidget:
        icon: root.icon


<PreviousMDIcons>
    id: coco
    canvas.before:
        PushMatrix:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
    canvas.after:
        PopMatrix:

    MDBoxLayout:
        orientation: 'vertical'
        #spacing: dp(10)
        #padding: dp(20)

        MDFloatLayout:
            adaptive_height: True
            md_bg_color: 1, 1, 1, 1
            size_hint: 1, 0.1

            TextInput:
                pos_hint: {"center_y": 0.5, "center_x": 0.5}
                on_text: coco.set_list_md_icons(self.text, True)
                multiline: False
                background_active: ""
                background_color: 1, 1, 1, 1
                background_disabled_normal: ""
                background_normal: ""
                cursor_color: 0, 0, 0, 1
                font_name: "fonts/Montserrat-Light.ttf"
                font_size: "12dp"
                hint_text: "Search"
                hint_text_color: 0, 0, 0, 1
                color: 0, 0, 0, 1
                padding: 45, 11.9
                size_hint_y: None
                size_hint_x: .97
                height: 40
                
                #size_hint: 1, 
                canvas.before:
                    Color:
                        rgba: get_color_from_hex("F3F6F6")
                    Line:
                        width: 1
                        rounded_rectangle: self.x, self.y, self.width, self.height, 10, 100

                    RoundedRectangle:
                        radius: [10]
                        size: self.size
                        pos: self.pos
                    Color:
                        rgba: 0, 0, 0,1 

            MDIconButton:
                icon: 'magnify'
                icon_color: 0, 0, 0, 1
                icon_size: '30dp'
                theme_icon_color: "Custom"
                pos_hint: {"center_x": 0.07, "center_y": 0.5}

            MDIconButton:
                icon: 'close'
                icon_color: 0, 0, 0, 1
                icon_size: '30dp'
                theme_icon_color: "Custom"
                pos_hint: {"center_x": 0.94, "center_y": 0.5}
            

            
               

        RecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'

            RecycleBoxLayout:
                #padding: dp(10)
                default_size: None, dp(80)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'


<ContactItem>:
    md_bg_color: 0.5, 0.8, 0.8, 1
    size_hint: 1, .15
    id: contactItem
    avatar: 'http://127.0.0.1:8000/media/images/avatars/1/filename.jpg'
    full_name: "Yekorogha Ayebatariwalate"
    user_id: "19010301043"
    Button:
        #text: "hello"
        id: CI
        background_normal: ""
        background_active: ""
        #background_down: ''
        #background_color: [1, 1, 1, 1]
        #on_press: self.background_color = (0.5, 0.5, 0.5, 0.2)
        #on_release: self.background_color = (1, 1,1 ,1)
        FitImage:
            source: contactItem.avatar
            size: CI.height - 10, CI.height - 10
            radius: [50]
            pos: CI.pos[0] + 10, CI.pos[1] + 5
        MDLabel:
            text: contactItem.full_name
            font_name: "fonts/arialmt.ttf"
            font_size: "19dp"
            size_hint_x: None
            width: 500
            pos: CI.pos[0] + 83, CI.pos[1]
        MDLabel:
            text: contactItem.user_id
            font_name: "fonts/Montserrat-Light.ttf"
            font_size: "15dp"
            pos: CI.pos[0] + 85, CI.pos[1] - 20






'''
)


class ContactItem(MDBoxLayout):
    avatar = StringProperty()
    full_name = StringProperty()
    user_id = StringProperty()

    def __init__(self, **kwargs):
        super(ContactItem, self).__init__(**kwargs)

class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()


contacts = [
    # avatar, full_name, user_id
    ["http://127.0.0.1:8000/media/default/account.png", "Olatubosun John", "19010301047"],
    ["http://127.0.0.1:8000/media/default/account.png", "Meshe Damilola-Peter", "19010301087"],
    ["http://127.0.0.1:8000/media/images/avatars/1/filename.jpg", "Yekorogha Tari", "19010301043"]
]


class PreviousMDIcons(Screen):

    def set_list_md_icons(self, text="", search=False):
        '''Builds a list of icons for the screen MDIcons.'''

        def add_contact_item(contact):
            self.ids.rv.data.append(
                {
                    "viewclass": "ContactItem",
                    "avatar": contact[0],
                    "full_name": contact[1],
                    "user_id": contact[2],
                }
            )

        self.ids.rv.data = []
        for contact in contacts:
            if search:
                # IT"S A STRING
                if text in contact[2]:
                    add_contact_item(contact)
            else:
                add_contact_item(contact)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = PreviousMDIcons()

    def build(self):
        return self.screen

    def on_start(self):
        self.screen.set_list_md_icons()


MainApp().run()