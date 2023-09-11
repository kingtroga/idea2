from kivymd.app import MDApp
from kivy.lang import Builder
from py.widgets.topbar import TopBar
from kivy.metrics import dp
from kivy.config import Config
Config.set('graphics', 'width', '380')
Config.set('graphics', 'height', '600')
Config.write()

Builder.load_file("kv/widgets/topbar.kv")

kv = """
FloatLayout:
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            size: self.size
            pos: self.pos
    Button:
        id: bottomNav
        size_hint: 1, 0.1
        pos_hint: {'x': 0}
        background_normal: ""
        background_down: ''
        background_color: 1, 1, 1, 1
    TextInput:
        id: messageBox
        pos_hint: {"center_y": 0.05, "center_x": 0.43}
        #on_text: coco.set_list_md_icons(self.text, True)
        multiline: False
        background_active: ""
        background_color: 1, 1, 1, 1
        background_disabled_normal: ""
        background_normal: ""
        cursor_color: 0, 0, 0, 1
        font_name: "fonts/Montserrat-Light.ttf"
        font_size: "12dp"
        hint_text: "Write Your Message"
        hint_text_color: get_color_from_hex("797C7B")
        color: 0, 0, 0, 1
        padding: 10, 11.9
        size_hint_y: None
        size_hint_x: .67
        height: 40
        #size_hint: 1, 
        canvas.before:
            Color:
                rgba: get_color_from_hex("F3F6F6")
            Line:
                width: 1
                rounded_rectangle: self.x, self.y, self.width, self.height, 10, 100

            RoundedRectangle:
                radius: [10]
                size: self.size
                pos: self.pos
            Color:
                rgba: get_color_from_hex("797C7B")

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

    
                    

            
            

 
        

            


"""


class TestApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

if __name__ == "__main__":
    TestApp().run()