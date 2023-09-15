from kivymd.app import MDApp
from kivy.metrics import dp

class TestApp(MDApp):
    def build(self):
        pass

    def caculate_width(self, widget):
        print(len(widget.text))
        _ = len(widget.text)
        return dp(_ * 10)

if __name__ == "__main__":
    TestApp().run()