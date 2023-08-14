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


    # FOR A NICE TRANSITION
    def slowMo(self, dt):
        self.app.root.current = "Screen7"

    def setHomeScreenToGroupChats(self, app):
        app.NAVIGATION = 'group_chats'
        app.root.screens[6].ids['NavBar'].goToAppNav(app)

    def setHomeScreenToPrivateChats(self, app):
        app.NAVIGATION = 'private_chats'
        app.root.screens[6].ids['NavBar'].goToAppNav(app)

    def setHomeScreenToAnnouncements(self, app):
        app.NAVIGATION = 'announcements'
        app.root.screens[6].ids['NavBar'].goToAppNav(app)

    def setHomeScreenToSettings(self, app):
        app.NAVIGATION = 'settings'
        app.root.screens[6].ids['NavBar'].goToAppNav(app)


    def goToHomeScreen(self, app):
        self.app = app
        Clock.schedule_once(self.slowMo, 0.7)