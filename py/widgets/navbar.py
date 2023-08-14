from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivy.clock import Clock

class NavBar(MDBottomNavigation):
    def __init__(self, **kwargs):
        super(NavBar, self).__init__(**kwargs)
        self.count = 0 
        #Clock.schedule_once(self.work, 1)

    def work(self, dt):
        print(self.ids)

    def goToFakeAnnoucements(self):
        self.switch_tab('fake_announcements')

    def goToAppNav(self, app):
        if app.NAVIGATION != None and self.count > 0:
            self.switch_tab(app.NAVIGATION)
            app.NAVIGATION = None
            self.count = self.count + 1