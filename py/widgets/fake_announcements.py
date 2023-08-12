from kivymd.uix.bottomnavigation import MDBottomNavigationItem
#from py.widgets.topbar import TopBar
from py.widgets.smoothbutton import SmoothButton
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.utils import get_color_from_hex

#Builder.load_file("kv\widgets\\topbar.kv")
Builder.load_file("kv\widgets\smoothbutton.kv")

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

    def handlePublishBtnPress(self, btn):
        btn.color = (121/255, 124/255, 123/255, 1)
        btn.back_color = (36/255, 120/255, 109/255, 1)

    def handlePublishBtnRelease(self, btn):
        btn.color = 1, 1, 1, 1
        btn.back_color = 32/255, 160/255, 144/255, 1


    def handleCancelBtnPress(self, btn):
        btn.color = get_color_from_hex("a23131")
        btn.back_color = (250/255, 1, 255/255, 1)

    def handleCancelBtnRelease(self, btn):
        btn.color = 220/255, 0, 0, 1
        btn.back_color = 241/255, 255/255, 253/255, 1 
    
    def changeToAnnouncementScreen(self, app):
        app.root.current = "Screen7"