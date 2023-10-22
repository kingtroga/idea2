from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout


class ContactItem(MDBoxLayout):
    avatar = StringProperty()
    full_name = StringProperty()
    user_id = StringProperty()

    def __init__(self, **kwargs):
        super(ContactItem, self).__init__(**kwargs)

    def changeToMessageScreen(self, contactitem, app):
        print(contactitem.user_id)
        print(contactitem.full_name)
        self.app = app
        #app.root.current = "Screen10"