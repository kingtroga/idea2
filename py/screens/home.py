from kivy.uix.screenmanager import Screen

class Home(Screen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        self.name = "Screen7"

    def checkAppNav(self, app):
        print(app.NAVIGATION)