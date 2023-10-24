from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
import requests

#PYTHON
from py.widgets.contactitem import ContactItem





class ContactsPage(Screen):
    
    def __init__(self, **kwargs):
        super(ContactsPage, self).__init__(**kwargs)
        self.name = "Screen11"
        self.app = MDApp.get_running_app()


    def set_list_md_icons(self, text="", search=False):
        '''Builds a list of icons for the screen MDIcons.'''

        def add_contact_item(contact):
            avatar_url = "https://atary.pythonanywhere.com/media/default/account.png"
            self.ids.rv.data.append(
                {
                    "viewclass": "ContactItem",
                    "avatar": avatar_url,
                    "full_name": contact['full_name'],
                    "user_id": str(contact['user_id']),
                }
            )

        self.ids.rv.data = []
        for contact in self.app.contacts:
            if search:
                # IT"S A STRING
                if text in str(contact['user_id']) or text in str(contact['full_name']):
                    add_contact_item(contact)
            else:
                add_contact_item(contact)

    def changeToHomeScreen(self, app):
        self.app = app
        self.app.root.current = "Screen7"

