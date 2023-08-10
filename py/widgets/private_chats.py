from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivy.clock import Clock
from PIL import Image
from py.widgets.imagebutton import ImageButton
from py.widgets.chatitem import ChatItem
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label.label import MDLabel
import threading

Builder.load_file("kv\widgets\imagebutton.kv")
Builder.load_file("kv\widgets\chatitem.kv")

class PrivateChats(MDBottomNavigationItem):
    def __init__(self, **kwargs):
        super(PrivateChats, self).__init__(**kwargs)
        self.appStart = True

        ##### HARD CODED STUFF FOR THE HOME PAGE
        self.user_list = {"1" : "image_1", "2" : "image_2", "3" : "image_3", 
                "4" : "image_4", "5" : "image_5", "6" : "image_6", }
        self.uppertext_list = {"1": "Dr. Balogun", "2": "300L Computer Sc..", 
                "3": "Abraham John", "4": "Shalom", 
                "5": "19010301024", "6":"Angel Dayna"}

        self.lowertext_list = {"1": "I haven't seen your assign...", "2":"There will be CSC 307 class...",
                "3": "Hey! Can you join the meeting?", "4": "How are you today?",
                "5": "Have a good day🌸", "6": "How are you today?"}

        self.timeline_list = {"1": "2 min ago", "2": "2 min ago", "3": "2 min ago",
                "4": "5 min ago", "5": "yesterday", "6": "2 min ago"}

        self.icon_list = {"1": "numeric-3-circle", "2": "numeric-4-circle", "3":"",
            "4":"", "5":"", "6":""}
        #################################################

        self.lock = threading.Lock()



##############################################################################################################################3
###########################STORIES#####################################################################################################
#########################################################################################################################################


    def _remove_loading(self, dt):
        self.loading = self.ids['loading']
        self.loading.opacity = 0
        

    def remove_loading(self):
        while True:
            with self.lock:
                if not self.appStart:
                    Clock.schedule_once(self._remove_loading, 1)
                    break

    def show_storys_and_chats(self):
        loading_thread = threading.Thread(target=self.remove_loading, daemon=True)
        loading_thread.start()
        if self.appStart:
            for i in self.user_list:
                img = Image.open(f'images\{i}.jpg')
                self.ids['grid'].add_widget(ImageButton(image_source=f"images\{i}.jpg", color_line=self.get_dominant_color(img)))
            
                self.ids['rv'].data.append({
                            'avatar' : f'images\{i}.jpg',
                            "uppertext": self.uppertext_list[i],
                            "lowertext": self.lowertext_list[i],
                            "timeline": self.timeline_list[i],
                            "icon": self.icon_list[i]
                        })
            self.appStart = False
  

    

    def get_dominant_color(self, pil_img, palette_size=16):
        # Resize image to speed up processing
        img = pil_img.copy()
        img.thumbnail((100, 100))

        # Reduce colors (uses k-means internally)
        paletted = img.convert('P', palette=Image.ADAPTIVE, colors=palette_size)

        # Find the color that occurs most often
        palette = paletted.getpalette()
        color_counts = sorted(paletted.getcolors(), reverse=True)
        palette_index = color_counts[0][1]
        dominant_color = palette[palette_index*3:palette_index*3+3]
        kivy_color = []
        for i in dominant_color:
            kivy_color.append(i/255)
        kivy_color.append(1)
        return kivy_color