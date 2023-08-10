from kivy.uix.screenmanager import Screen, WipeTransition, NoTransition
from kivy.clock import Clock
from kivy.animation import Animation


class Onboarding(Screen):
    def __init__(self, **kwargs):
        super(Onboarding, self).__init__(**kwargs)
        self.name  = "Screen 3"

    def changeScreenToSignUpScreen(self, *args):
        self.manager.transition = NoTransition()
        self.manager.current = "Screen4"

    def changeScreenToLoginInScreen(self, *args):
        self.manager.transition = NoTransition()
        self.manager.current = "Screen5"