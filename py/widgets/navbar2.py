from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivy.clock import Clock

from py.widgets.navbar import NavBar




class NavBar2(MDBottomNavigation):
    def __init__(self, **kwargs):
        super(NavBar2, self).__init__(**kwargs)
        
        Clock.schedule_once(self.work, 9)
        # self.ids['tab_manager'] = self.sm

    def work(self, dt):
        self.switch_tab('fake_announcements')

    def goToFakeAnnouncements(self):
        self.switch_tab('fake_announcements')

    def goToRealGroupChats(self, dt):
        self.app.root.current = "Screen7"

    def setHomeScreenToGroupChats(self, app):
        app.NAVIGATION = 'group_chats'
        app.root.screens[6].ids['NavBar'].goToAppNav(app)

    def goToHomeScreen(self, app):
        self.app = app
        Clock.schedule_once(self.goToRealGroupChats, 1)