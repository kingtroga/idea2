from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from py.widgets.header import Header
from py.widgets.bubbleitem import BubbleItem

Builder.load_file("kv\widgets\header.kv")
Builder.load_file("kv\widgets\\bubbleitem.kv")

class CreateGroup(Screen):
    def __init__(self, **kwargs):
        super(CreateGroup, self).__init__(**kwargs)
        self.name  = "Screen8"

    def changeScreenToGroupChatsScreen(self, app):
        app.root.current = "Screen7"
