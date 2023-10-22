from kivymd.app import MDApp
from kivy.lang import Builder
from py.widgets.topbar import TopBar
from kivy.metrics import dp
from kivy.config import Config
from kivy.clock import Clock
Config.set('graphics', 'width', '380')
Config.set('graphics', 'height', '600')
Config.write()
from kivy.utils import get_color_from_hex

from py.widgets.messagebox import MessageBox
from py.widgets.chatitem import ChatItem
from py.widgets.messageitem import MessageItem
Builder.load_file("kv/widgets/messagebox.kv")
Builder.load_file("kv/widgets/chatitem.kv")
from kivy.core.window import Window
import websocket


kv = """
FloatLayout:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos


    

    Button:
        id: TopNav
        size_hint: 1, 0.1
        pos_hint: {'x': 0, "top": 1}
        background_normal: ""
        background_down: ''
        background_color: 1, 1, 1, 1
        canvas.after:
            Color:
                rgba: (238/255, 250/255, 248/255, 1)
            Line:
                width: 1
                rounded_rectangle: self.x, self.y, self.width, self.height, 0, 100

        MDLabel:
            text: "Yekorogha A"
            font_size: dp(20)
            color: 0, 0, 0, 1
            #pos_hint: {"center_x": 0.78, "center_y": 0.965}
            bold: True
            size_hint: None, None
            width: 500
            font_name: "fonts/arialmt.ttf"
            pos: self.parent.pos[0] + dp(110), self.parent.pos[1] - dp(11)

        MDLabel:
            text: "Active Now"
            font_size: dp(15)
            color: get_color_from_hex("797C7B")
            pos_hint: {"center_x": 0.78, "center_y": 0.92}
            bold: True
            font_name: "fonts/Montserrat-Light.ttf"
            pos: self.parent.pos[0] + dp(110), self.parent.pos[1] - dp(33)

    MDIconButton:
        icon: 'arrow-left'
        icon_color: get_color_from_hex("000E08")
        icon_size: '18dp'
        theme_icon_color: "Custom"
        pos: TopNav.pos[0], TopNav.pos[1] + dp(8)

    
    MDIconButton:
        icon: 'account'
        icon_size: '35dp'
        theme_icon_color: "Custom"
        pos: TopNav.pos[0] + dp(45), TopNav.pos[1] + dp(2.5)
        icon_color: 0, 0, 0, 1
        canvas.before:
            Color:
                rgba: (0, 0, 0, 1)
            Line:
                width: 1
                ellipse: self.pos[0] + 5, self.pos[1] + 3, self.size[0] - 10, self.size[1] - 10

        

    MDIconButton:
        icon: 'phone-outline'
        icon_color: get_color_from_hex("000E08")
        icon_size: '30dp'
        theme_icon_color: "Custom"
        pos: TopNav.width - dp(110), TopNav.pos[1] + dp(2.5)

    MDIconButton:
        icon: 'video-outline'
        icon_color: get_color_from_hex("000E08")
        icon_size: '30dp'
        theme_icon_color: "Custom"
        pos: TopNav.width - dp(60), TopNav.pos[1] + dp(2.5)




    
    







   
        

        









    Button:
        id: bottomNav
        size_hint: 1, 0.1
        pos_hint: {'x': 0}
        background_normal: ""
        background_down: ''
        background_color: 1, 1, 1, 1
        canvas.after:
            Color:
                rgba: (238/255, 250/255, 248/255, 1)
            Line:
                width: 1
                rounded_rectangle: self.x, self.y, self.width, self.height, 0, 100
    
    MessageBox:
        id: messageBox
        on_text_validate: self.printMessage()

    MDIconButton:
        icon: 'paperclip'
        icon_color: get_color_from_hex("000E08")
        icon_size: '30dp'
        theme_icon_color: "Custom"
        pos: messageBox.pos[0] - dp(40), messageBox.pos[1] - dp(5)


    MDIconButton:
        icon: 'file-multiple-outline'
        icon_color: get_color_from_hex("797C7B")
        icon_size: '30dp'
        theme_icon_color: "Custom"
        pos: messageBox.width - dp(5), messageBox.pos[1] - dp(5)

    MDIconButton:
        icon: 'camera-outline'
        icon_color: get_color_from_hex("000E08")
        icon_size: '30dp'
        theme_icon_color: "Custom"
        pos: messageBox.width + dp(37), messageBox.pos[1] - dp(5)


    MDIconButton:
        icon: 'microphone-outline'
        icon_color: get_color_from_hex("000E08")
        icon_size: '30dp'
        theme_icon_color: "Custom"
        pos: messageBox.width + dp(74), messageBox.pos[1] - dp(5)


    MDFloatLayout:
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint: 1, 0.795
        md_bg_color: 1, 1, 1, 1
        ScrollView:
            do_scroll_x: False
            do_scroll_y: True
            size_hint: 1, None
            size: self.parent.width, self.parent.height
            pos: self.parent.pos[0], self.parent.pos[1]
            MDFloatLayout:
                md_bg_color: 1, 1, 1, 1
                id: aBox
                size_hint_y: None
                size_hint_x: 1
                height: 1400




    
                    

            
            

 
        

            


"""


class TestApp(MDApp):
    def build(self):
        return Builder.load_string(kv)
    
    

    
    
    
       

if __name__ == "__main__":
    TestApp().run()