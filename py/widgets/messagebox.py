from kivy.uix.textinput import TextInput
from kivymd.app import MDApp

from py.widgets.chatitem import ChatItem

from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty
from kivy.core.window import Window 
from kivymd.uix.label import MDLabel
from kivy.metrics import dp
Builder.load_file('kv\widgets\messageitem.kv')


class MessageItem(MDLabel):
    color = ListProperty()
    atext = StringProperty()

    def __init__(self, **kwargs):
        super(MessageItem,self).__init__(**kwargs)
        self.font_name = "fonts/Montserrat-Light.ttf"
        self.color = [1, 1, 1, 1]
    
    def caculate_width(self, widget):
        #if len(widget.text)
        if len(widget.text) == 5:
            return dp(0.15)
        elif len(widget.text) == 1:
            return dp(0.08)
        elif len(widget.text) == 4:
            return dp(0.13)
        
        elif len(widget.text) <= 36:
            _ = len(widget.text)
            return dp(round((_/Window.width * 10), 1))
        else:
            return dp(0.6)
    
    def caculate_height(self, widget):
        if len(widget.text) <= 25:
            return dp(0.038)
        elif  47 <= len(widget.text) <= 55:
            return dp(0.053)
        else:
            return dp(round((len(widget.text)/(Window.height*2.5)), 1))

class MessageBox(TextInput):
    def __init__(self, **kwargs):
        super(MessageBox, self).__init__(**kwargs)
        self.counter = 1

    
    def printMessage(self):
        # CREATE THE MESSAGE
        self.msg = MessageItem(atext=self.text, pos_hint={ "top":self.counter, "right": 0.98}, font_name="fonts/Montserrat-Light.ttf")
        
        #SPACING
        self.counter = round((self.counter - 0.03),2)
        
        # SCROLL VIEW
        self.parent.children[0].children[0].children[0].add_widget(self.msg)
        
        # RESET THE MESSAGE BOX
        self.text = ""

        # FOR GOOD SPACING (Limit the input to 50 characters)
        if len(self.msg.text) >= 50:
            self.counter = round((self.counter - 0.016),2)
        
        
        