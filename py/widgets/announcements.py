from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from py.widgets.announcementitem import AnnouncementItem
from kivy.lang import Builder
from kivy.clock import Clock
import threading

Builder.load_file("kv\widgets\\announcementitem.kv")

class Announcements(MDBottomNavigationItem):
    def __init__(self, **kwargs):
        super(Announcements, self).__init__(**kwargs)
        #Clock.schedule_interval(self.work, 1)
        self.newAn = True
        self.lock = threading.Lock()
        ###########################################################################################
        ############################### ANNOUNCEMENTITEM STUFF ####################################
        ###########################################################################################
        self.author_list = [1, 2, 3]
        self.author_names = {1 : "Ajibade Benjamin", 2 : "Dr. Kasali", 3 : "J. Balogun"}
        self.date_created = {1 : "Today, 09:30AM", 2 : "Today, 9:30AM", 3: "Today, 9:30AM"}
        self.anTopic = {1: "Change of Venue For Exam", 2:"CSC 409 Make-Up Test", 3:"CSC 406 Class Is Holding!"}
        self.anContent = {
                1: "This is a notice to all 400 level students that offer CSC 411 that the venue for the exam is no longer LTB 1, it's now BIG LT",
                2: "This is a notice to all 400 level students that offer CSC 411 that the venue for the exam is no longer LTB 1, it's now BIG LT",
                3: "Good Afternoon to all 400 level students that offer CSC 406. There will be CSC 406 class by 10pm today unfailingly. Ensure to be there because attendance will be taken"
                }

    def _remove_loading(self, dt):
        self.loading = self.ids['loading']
        self.loading.opacity = 0

    def remove_loading(self):
        while True:
            with self.lock:
                if not self.newAn:
                    Clock.schedule_once(self._remove_loading, 1)
                    break


    def show_announcements(self):
        loading_thread = threading.Thread(target=self.remove_loading, daemon=True)
        loading_thread.start()
        if self.newAn:
            for i in self.author_list:
                self.ids['aBox'].add_widget(
                    AnnouncementItem(
                        avatar=f"images/{i}.jpg", 
                        author_name=self.author_names[i],
                        date_created=self.date_created[i],
                        topic=self.anTopic[i],
                        body=self.anContent[i])
                    )
            self.newAn = False

