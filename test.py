from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_file("kv/widgets/messageitem.kv")
from py.widgets.messageitem import MessageItem

class TestApp(MDApp):
    def build(self):
        pass

    

if __name__ == "__main__":
    TestApp().run()