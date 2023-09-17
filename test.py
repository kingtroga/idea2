from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.core.window import Window

class TestApp(MDApp):
    def build(self):
        pass

    def caculate_width(self, widget):
        if len(widget.text) <= 36:
            # 0.15
            print(len(widget.text))
            print(Window.width)
            _ = len(widget.text)
            print(dp(_/Window.width))
            print(dp(_/Window.width * 10))
            return dp(_/Window.width * 10)
        else:
            return dp(0.6)
    
    def caculate_height(self, widget):
        if len(widget.text) <= 36:
            print(Window.height)
            _ = len(widget.text)
            print(widget.size)
            return dp(0.08)
        else:
            print(dp(len(widget.text)/Window.width))
            #print(widget.size)
            #TODO: ROUND UP TO ONE DECIMAL PLACE
            return dp(len(widget.text)/Window.width)
    

    

if __name__ == "__main__":
    TestApp().run()