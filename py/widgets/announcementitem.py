from kivymd.uix.label.label import MDFloatLayout
from kivy.properties import StringProperty
from kivy.clock import Clock


class AnnouncementItem(MDFloatLayout):
    avatar = StringProperty()
    author_name = StringProperty()
    date_created = StringProperty()
    topic = StringProperty()
    body = StringProperty()

    def __init__(self, **kwargs):
        super(AnnouncementItem, self).__init__(**kwargs)
        #Clock.schedule_once(self.work, 1)

    #def work(self, dt=None):
    #    print(self.ids['author_name'].pos)
