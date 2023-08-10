from kivy.uix.boxlayout import BoxLayout
from kivy.properties import (
    StringProperty, 
    NumericProperty,
    BooleanProperty,
    ListProperty,
)
from kivy.utils import get_color_from_hex
    

class ChatItem(BoxLayout):
    avatar = StringProperty()
    uppertext = StringProperty()
    lowertext = StringProperty()
    timeline = StringProperty()
    icon = StringProperty()
    icon_size = NumericProperty()
    is_bold = BooleanProperty()
    text_icon_dis = NumericProperty()
    uppertextY = NumericProperty()
    lowertextY = NumericProperty()
    back_color = ListProperty()
    font_fam1 = StringProperty()