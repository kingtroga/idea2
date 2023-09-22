from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import StringProperty, ListProperty, BooleanProperty

class MessageItem(MDLabel):
    color = ListProperty()
    atext = StringProperty()
    inMessage = BooleanProperty()

    def __init__(self, **kwargs):
        super(MessageItem,self).__init__(**kwargs)
        
    
    def caculate_width(self, widget):
        if len(widget.text) <= 36:
            _ = len(widget.text)
            return dp(round((_/Window.width * 10), 2))
        else:
            return dp(0.6)
    
    def caculate_height(self, widget):
        if len(widget.text) <= 36:
            return dp(0.08)
        else:
            return dp(round((len(widget.text)/Window.width), 2))
