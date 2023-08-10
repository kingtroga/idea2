from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse
from kivy.clock import Clock
import math

class CircularMotionApp(App):
    def build(self):
        self.circle_center_x = 300
        self.circle_center_y = 300
        self.circle_max_radius = 200
        self.circle_min_radius = 50
        self.angle = 0
        self.distance = 50  # Adjust the distance between the two circles here

        self.circle_widget = Widget()

        self.circle1 = Ellipse(pos=(self.circle_center_x - self.circle_max_radius, self.circle_center_y - self.circle_max_radius),
                               size=(self.circle_max_radius * 2, self.circle_max_radius * 2), source='green.png')
        self.circle_widget.canvas.add(self.circle1)

        self.circle2 = Ellipse(pos=(self.circle_center_x - self.circle_max_radius - self.distance,
                                    self.circle_center_y - self.circle_max_radius - self.distance),
                               size=(self.circle_max_radius * 2, self.circle_max_radius * 2), source='red.png')
        self.circle_widget.canvas.add(self.circle2)

        # Schedule the update function to be called every 0.01 seconds (you can adjust the time interval)
        Clock.schedule_interval(self.update, 0.01)

        return self.circle_widget

    def update(self, dt):
        # Calculate the new position based on the angle and radius
        self.angle += 0.05  # You can adjust the speed of the circular motion by changing this value
        x1 = self.circle_center_x + self.circle_max_radius * math.cos(self.angle)
        y1 = self.circle_center_y + self.circle_max_radius * math.sin(self.angle)

        x2 = self.circle_center_x + (self.circle_max_radius + self.distance) * math.cos(self.angle)
        y2 = self.circle_center_y + (self.circle_max_radius + self.distance) * math.sin(self.angle)

        # Update the position of the circles
        self.circle1.pos = (x1 - self.circle_max_radius, y1 - self.circle_max_radius)
        self.circle2.pos = (x2 - self.circle_max_radius, y2 - self.circle_max_radius)

if __name__ == '__main__':
    CircularMotionApp().run()
