from kivymd.uix.bottomnavigation import MDBottomNavigationItem

class FakeSettings(MDBottomNavigationItem):
    def __init__(self, **kwargs):
        super(FakeSettings, self).__init__(**kwargs)