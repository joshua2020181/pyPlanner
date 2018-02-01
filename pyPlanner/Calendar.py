# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:01:36 2017

@author: joshc + connerm
"""
from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import *
import main
from kivy.uix.widget import Widget

class Calendar(FloatLayout):
    def __init__(self, **kwargs):
        super(Calendar, self).__init__(**kwargs)
        def colorSelector(decValue):
            result = []
            for x in decValue:
                result.append(x / 255)
            result.append(1)
            return result
        def dCallback(instance, value):
            if(value == 'down'):
                self.clear_widgets()
                main.dPressed()
        with self.canvas:       # set background
            Color(.9, .9, .9)
            Rectangle(pos_hint={'x':.5, 'y':.5}, size=(100000, 100000))
        with self.canvas:
            # Add a red color
            Color(1, 0, 0)
            # Add a rectangle
            Rectangle(pos=(0, 600), size=(1500, 2))
            
        # Title
        title = Label(pos_hint={'x':0, 'y':.4}, text = '[color=0055ff][font=5thgradecursive]Calendar[/font][/color]', font_size='60sp', markup = True)
        self.add_widget(title)
        # Week button
        week = Button(pos_hint={'x':0, 'y':.6501}, size_hint=(.24,.12), text = 'Week', font_size='30sp', background_color= colorSelector([160,32,240]), markup = True)
        week.bind(state=dCallback)
        self.add_widget(week)
        # Month button
        month = Button(pos_hint={'x':0, 'y':.375}, size_hint=(.24,.12), text = 'Month', font_size='30sp', background_color = colorSelector([0, 255, 0]), markup = True)
        self.add_widget(month)
        # Back button
        back = Button(pos_hint={'x':0, 'y':0.9}, size_hint=(.24,.12), text = 'Back', font_size='30sp', background_color = colorSelector([0, 0, 0]), markup = True)
        self.add_widget(back)
        back.bind(state=dCallback)
        
        '''self.add_widget(Label(text="Password:"))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

        self.add_widget(Label(text="Two Factor Auth:"))
        self.tfa = TextInput(multiline=False)
        self.add_widget(self.tfa)
'''
		

class SimpleKivy(App):
    def build(self):
        return Calendar()

if __name__ == "__main__":
    SimpleKivy().run()		