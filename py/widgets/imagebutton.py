from kivymd.uix.button.button import MDIconButton
from kivy.properties import StringProperty, ListProperty

class ImageButton(MDIconButton):
    image_source = StringProperty()
    color_line = ListProperty()