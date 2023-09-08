from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.label.label import MDFloatLayout
from py.widgets.groupinfo import GroupInfo
from py.widgets.chatitem import ChatItem
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
import threading


class GroupChats(MDBottomNavigationItem):
    def __init__(self, **kwargs):
        super(GroupChats, self).__init__(**kwargs)
        self.groupACTIVE = False
        self.lock = threading.Lock()
        self.group_icon_list = {7, 8, 9}
        self.group_uppertext_list = {7: "400L Computer Science", 8: "300L CSC",
                            9: "Cyber Security" }
        self.group_lowertext_list = {7: "Final Year Brethren", 8: "Keep working✍🏾",
                            9: "200 L Cyber Security Students"}
        #Clock.schedule_once(self.show_groups, 0.5)

    def show_groups(self, dt=None):
        loading_thread = threading.Thread(target=self.remove_loading, daemon=True)
        loading_thread.start()
        layout = MDFloatLayout(size_hint=(1, 0.34), md_bg_color=get_color_from_hex("#FFFFFF"))
        layout.add_widget(GroupInfo())
        if not self.groupACTIVE:
            for i in self.group_icon_list:
                self.ids['groupie'].add_widget(
                    ChatItem(
                        avatar=f'images/{i - 2}.jpg',
                        uppertext=self.group_uppertext_list[i],
                        lowertext=self.group_lowertext_list[i],
                        timeline="",
                        icon=""
                    ))
            self.ids['groupie'].add_widget(layout)
            self.groupACTIVE = True

    def remove_loading(self):
        while True:
            with self.lock:
                if self.groupACTIVE:
                    Clock.schedule_once(self._remove_loading, 1)
                    break

    def _remove_loading(self, dt):
        self.loading = self.ids['loading']
        self.loading.opacity = 0


    def printHello(self):
        print("Hello")

    def changeScreenToCreateGroupScreen(self, app):
        app.root.current = "Screen8"
        


