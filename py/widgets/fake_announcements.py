from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from py.widgets.topbar import TopBar
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_file("kv\widgets\\topbar.kv")

class FakeAnnouncements(MDBottomNavigationItem):
    def __init__(self, **kwargs):
        super(FakeAnnouncements, self).__init__(**kwargs)
        Clock.schedule_once(self.getIDs, 0.5)

    def getIDs(self, dt):
        self.backButton1 = self.ids['background-1']
        self.backButton2 = self.ids['background-2']
        self.backButton3 = self.ids['background-3']


    def showBackSelection(self):
        # Background Button 1
        if self.backButton1.state == "down":
            self.backButton1.line_color = (205/255, 202/255, 202/255, 1)
        elif self.backButton1.state == "normal":
            self.backButton1.line_color = (1, 1, 1, 1)

        # Background Button 2
        if self.backButton2.state == "down":
            self.backButton2.line_color = (205/255, 202/255, 202/255, 1)
        elif self.backButton2.state == "normal":
            self.backButton2.line_color = (1, 1, 1, 1)

        # Background Button 3
        if self.backButton3.state == "down":
            self.backButton3.line_color = (205/255, 202/255, 202/255, 1)
        elif self.backButton3.state == "normal":
            self.backButton3.line_color = (1, 1, 1, 1)   