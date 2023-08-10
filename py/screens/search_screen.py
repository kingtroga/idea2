from kivy.uix.screenmanager import Screen

class SearchScreen(Screen):
    def __init__(self, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)
        self.name  = "Screen3"