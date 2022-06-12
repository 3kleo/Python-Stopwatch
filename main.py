import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from datetime import datetime
import time
from threading import Timer
from kivy.clock import Clock


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.started = None
        self.num = 1

    def start_timer(self):
        if self.btn_1.text == 'Start':
            self.btn_1.text = "Pause"
            self.started = Clock.schedule_interval(self.time_counter, 1)
        else:
            self.btn_1.text = "Start"
            Clock.unschedule(self.started)
        
    def stop_timer(self):
        self.btn_1.text = "Start"
        Clock.unschedule(self.started)
        self.num = 1
        self.display.text = '00:00:00'

    def time_counter(self, dt):
        self.display.text = time.strftime('%H:%M:%S', time.gmtime(self.num))
        self.num += 1
        return


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
