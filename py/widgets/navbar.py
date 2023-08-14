from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivy.clock import Clock

class NavBar(MDBottomNavigation):
    def __init__(self, **kwargs):
        super(NavBar, self).__init__(**kwargs)
        #Clock.schedule_once(self.work, 1)



    def goToAppNav(self, app):
        if app.NAVIGATION != None:
            self.switch_tab(app.NAVIGATION)
            app.NAVIGATION = None