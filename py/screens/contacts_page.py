from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
import requests





class ContactsPage(Screen):
    
    def __init__(self, **kwargs):
        super(ContactsPage, self).__init__(**kwargs)
        self.name = "Screen11"
        self.app = MDApp.get_running_app()


    def set_list_md_icons(self, text="", search=False):
        '''Builds a list of icons for the screen MDIcons.'''

        def add_contact_item(contact):
            avatar_url = lambda contact: contact['avatar'] if contact['avatar'] is not None else "http://127.0.0.1:8000/media/default/account.png"
            self.ids.rv.data.append(
                {
                    "viewclass": "ContactItem",
                    "avatar": avatar_url(contact),
                    "full_name": contact['fullName'],
                    "user_id": str(contact['userID']),
                }
            )

        self.ids.rv.data = []
        for contact in self.app.contacts:
            if search:
                # IT"S A STRING
                if text in str(contact['userID']):
                    add_contact_item(contact)
            else:
                add_contact_item(contact)

    def changeToHomeScreen(self, app):
        self.app = app
        self.app.root.current = "Screen7"

class ContactItem(MDBoxLayout):
    avatar = StringProperty()
    full_name = StringProperty()
    user_id = StringProperty()

    def __init__(self, **kwargs):
        super(ContactItem, self).__init__(**kwargs)
