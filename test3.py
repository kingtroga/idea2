from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem

from kivymd.uix.fitimage import FitImage
from kivymd.uix.boxlayout import MDBoxLayout



 

Builder.load_string(
'''
#:import images_path kivymd.images_path


<CustomOneLineIconListItem>

    IconLeftWidget:
        icon: root.icon


<PreviousMDIcons>
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
        spacing: dp(10)
        #padding: dp(20)

        MDBoxLayout:
            adaptive_height: True
            md_bg_color: 0.6, 0.7, 0.9, 1

            MDIconButton:
                icon: 'magnify'

            MDTextField:
                id: search_field
                hint_text: 'Search icon'
                on_text: root.set_list_md_icons(self.text, True)

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
        ContactItem:

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