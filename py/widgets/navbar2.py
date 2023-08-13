from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivy.clock import Clock

class NavBar2(MDBottomNavigation):
    def __init__(self, **kwargs):
        super(NavBar2, self).__init__(**kwargs)
        
        Clock.schedule_once(self.work, 9)
        # self.ids['tab_manager'] = self.sm

    def work(self, dt):
        self.switch_tab('fake_announcements')

    def goToFakeAnnoucements(self):
        self.switch_tab('fake_announcements')