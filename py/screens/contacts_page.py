from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout


contacts = [
    # avatar, full_name, user_id
    ["http://127.0.0.1:8000/media/default/account.png", "Olatubosun John", "19010301047"],
    ["http://127.0.0.1:8000/media/default/account.png", "Meshe Damilola-Peter", "19010301087"],
    ["http://127.0.0.1:8000/media/images/avatars/1/filename.jpg", "Yekorogha Tari", "19010301043"]
]


class ContactsPage(Screen):
    
    def __init__(self, **kwargs):
        super(ContactsPage, self).__init__(**kwargs)
        self.name = "Screen11"

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

    def changeToHomeScreen(self, app):
        self.app = app
        self.app.root.current = "Screen7"

class ContactItem(MDBoxLayout):
    avatar = StringProperty()
    full_name = StringProperty()
    user_id = StringProperty()

    def __init__(self, **kwargs):
        super(ContactItem, self).__init__(**kwargs)
