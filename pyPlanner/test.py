# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:01:36 2017

@author: joshc
"""
from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput



class Dashboard(GridLayout):
    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)
        self.cols = 3
        self.add_widget(Label(text="Username:"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text="Password:"))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

        self.add_widget(Label(text="Two Factor Auth:"))
        self.tfa = TextInput(multiline=False)
        self.add_widget(self.tfa)

		

class SimpleKivy(App):
    def build(self):
        return Dashboard()

if __name__ == "__main__":
    SimpleKivy().run()		