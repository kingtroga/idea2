from kivy.uix.screenmanager import Screen, NoTransition
from kivy.animation import Animation
from kivy.metrics import dp


class SplashScreenTwo(Screen):
    def __init__(self, **kwargs):
        super(SplashScreenTwo, self).__init__(**kwargs)
        self.name  = "Screen2"

    def on_enter(self):
        ideaLabel = self.ids['ideaLabel1']
        ideaLabel_anim = Animation(pos_hint = {'center_y':0.97, 'center_x': 0.5},font_size=dp(30), duration=0.5)
        ideaLabel_anim.bind(on_complete=self.changeScreenToOnboardingScreen)
        ideaLabel_anim.start(ideaLabel)

    def changeScreenToOnboardingScreen(self, instance, value):
        self.manager.transition = NoTransition()
        self.manager.current = "Screen 3"
    
    
        