from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

class ChatItem(BoxLayout):
    avatar = StringProperty()
    uppertext = StringProperty()
    lowertext = StringProperty()
    timeline = StringProperty()
    icon = StringProperty()
