from kivymd.uix.bottomnavigation import MDBottomNavigationItem

class FakePrivateChats(MDBottomNavigationItem):
    def __init__(self, **kwargs):
        super(FakePrivateChats, self).__init__(**kwargs)