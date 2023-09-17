from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import RoundedRectangle, Color
from kivy.core.window import Window

class MyKivyApp(MDApp):
    def build(self):
        layout = FloatLayout()
        
        label = MDLabel(text="yoghurt")
        label.width, label.height = self.calculate_label_size(label)

        rr_width, rr_height, rr_x, rr_y = self.calculate_rr_size_and_pos(label)
        
        with label.canvas.before:
            Color(rgba=(0.5, 0.5, 0.5, 1))
            RoundedRectangle(pos=(rr_x, rr_y), size=(rr_width, rr_height), radius=[10, 0, 10, 10])
        
        layout.add_widget(label)
        
        return layout
    
    def calculate_label_size(self, label):
        # Calculate the width and height based on size_hint_x and size_hint_y
        width = label.size_hint_x * Window.width if label.size_hint_x is not None else label.width
        height = label.size_hint_y * Window.height if label.size_hint_y is not None else label.height
        return width, height
    
    def calculate_rr_size_and_pos(self, label):
        label_width, label_height = self.calculate_label_size(label)
        
        # Calculate RR size
        rr_width = label_width + 10
        rr_height = label_height - 20

        # Calculate RR position
        rr_x = label.pos[0] - 5
        rr_y = label.pos[1] + 10

        return rr_width, rr_height, rr_x, rr_y



if __name__ == '__main__':
    MyKivyApp().run()
