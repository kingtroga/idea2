from kivy.uix.screenmanager import Screen

class CreateGroup(Screen):
    def __init__(self, **kwargs):
        super(CreateGroup, self).__init__(**kwargs)
        self.name  = "Screen2"
