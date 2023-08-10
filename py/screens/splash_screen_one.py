from kivy.uix.screenmanager import Screen, WipeTransition
from kivy.clock import Clock
from kivy.animation import Animation


class SplashScreenOne(Screen):
    def __init__(self, **kwargs):
        super(SplashScreenOne, self).__init__(**kwargs)
        self.name  = "Screen1"
        

        
    
    def on_touch_down(self, touch):
        self.animateIdeaLabel1()
        pass

    def animateIdeaLabel1(self):
        idealabel1 = self.ids['ideaLabel1']
        anim = Animation(pos_hint={'center_x': 0.45}, duration=0.2)
        anim.bind(on_complete=self.animateIdeaLabel2)
        anim.start(idealabel1)

    def animateIdeaLabel2(self,instance, value):
        idealabel1 = self.ids['ideaLabel1']
        anim = Animation(pos_hint={'center_x': 0.5}, duration=0.2)
        anim.bind(on_complete=self.switchScreentoSplashScreenTwo)
        anim.start(idealabel1)

    def switchScreentoSplashScreenTwo(self, instance, value):
        self.manager.transition = WipeTransition()
        self.manager.current = "Screen2"
        

        
        


 