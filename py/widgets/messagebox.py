from kivy.uix.textinput import TextInput

class MessageBox(TextInput):
    def __init__(self, **kwargs):
        super(MessageBox, self).__init__(**kwargs)

    def keyboard_on_key_down(self, window, keycode, text, modifiers):
        if keycode[0] == 13:
            self.text = ""
        return super().keyboard_on_key_down(window, keycode, text, modifiers)