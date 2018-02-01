# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:01:36 2017

@author: joshc
"""
from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import *
from kivy.uix.widget import Widget
#import main
from kivy.uix.screenmanager import ScreenManager, Screen
#import Settings



class DashboardSc(Screen):
    def __init__(self, **kwargs):
        print('here')
        super(DashboardSc, self).__init__(**kwargs)
        sc = FloatLayout()
        def colorSelector(decValue):  #255,255,255 -> 1,1,1,1 (rgb -> rgba)
            result = []
            for x in decValue:
                result.append(x / 255)
            result.append(1)
            return result
        def assPressed(instance, value):
            if(value == 'down'):
                sc.clear_widgets()
                import main
                main.assPressed()
        def calPressed(instance, value):
            if(value == 'down'):
                sc.clear_widgets()
                import main
                main.calPressed()
        def settingsPressed(instance, value):
            if(value == 'down'):
                #sc.clear_widgets()
                import main
                #main.settingsPressed()
                main.sm.current = 'start'
            return None
        with sc.canvas:       # set background
            Color(.9, .9, .9)
            Rectangle(pos_hint={'x':.5, 'y':.5}, size=(100000, 100000))
        title = Label(pos_hint={'x':0, 'y':.4}, text = '[color=0055ff][font=Hobo]PyPlanner[/font][/color]', font_size='60sp', markup = True)
        sc.add_widget(title)
        
        ass = Button(pos_hint={'x':0, 'y':.65}, size_hint=(.24,.12), text = '[font=Hobo]Assignments[/font]', font_size='30sp', background_color=colorSelector([160,32,240]), markup = True)
        ass.bind(state=assPressed)
        sc.add_widget(ass)
        
        cal = Button(pos_hint={'x':0, 'y':.375}, size_hint=(.24,.12), text = '[font=Hobo]Calendar[/font]', font_size='30sp', background_color=colorSelector([0, 255, 0]), markup = True)
        sc.add_widget(cal)
        cal.bind(state=calPressed)
        
        settings = Button(pos_hint={'x':0, 'y':.1}, size_hint=(.24,.12), text = '[font=Hobo]Settings[/font]', font_size='30sp', background_color=colorSelector([255, 10, 10]), markup = True)
        sc.add_widget(settings)
        settings.bind(state=settingsPressed)
        self.add_widget(sc)
        '''self.add_widget(Label(text="Password:"))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)

        self.add_widget(Label(text="Two Factor Auth:"))
        self.tfa = TextInput(multiline=False)
        self.add_widget(self.tfa)
'''
		

class SimpleKivy(App):
    def build(self):
        return Dashboard(name='Dash')

if __name__ == "__main__":
    SimpleKivy().run()		