from kivymd.uix.bottomnavigation import MDBottomNavigationItem

class FakeGroupChats(MDBottomNavigationItem):
    def __init__(self, **kwargs):
        super(FakeGroupChats, self).__init__(**kwargs)