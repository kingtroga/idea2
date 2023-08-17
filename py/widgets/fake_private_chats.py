from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineAvatarListItem



class Item(OneLineAvatarListItem):
    divider = None
    source = StringProperty()
    userID = StringProperty()

class FakePrivateChats(MDBottomNavigationItem):
    def __init__(self, **kwargs):
        super(FakePrivateChats, self).__init__(**kwargs)
        self.dialog = None

    def show_simple_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Set backup account",
                type="simple",
                items=[
                    Item(text="user01@gmail.com", source="http://127.0.0.1:8000/media/images/avatars/1/filename.jpg"),
                    Item(text="user02@gmail.com", source="data/logo/kivy-icon-128.png", userID="19010301043"),
                ],
            )
        self.dialog.open()
