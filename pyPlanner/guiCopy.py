# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:01:36 2017

@author: joshua_cheng + conner_morgan
"""
from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import *
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.clock import Clock
import time
import timeit
from main import *

CalendarData.year = DateTime.year
CalendarData.month = DateTime.month

Builder.load_string("""
<StartScreen>:
    BoxLayout:
        Button:
            text: 'Start!'
            on_press: root.manager.current = 'Dashboard'
        Button:
            text: 'Quit'
            on_press: settingsPressed()
""")

class Calendar(Screen):
    def __init__(self, **kwargs):
        super(Calendar, self).__init__(**kwargs)
        sc = GridLayout(cols = 7, rows = 7)
        def colorSelector(decValue):  #255,255,255 -> 1,1,1,1 (rgb -> rgba)
            result = []
            for x in decValue:
                result.append(x / 255)
            result.append(1)
            return result
            return None
        def upPressed(instance, value):
            if value == 'down':
                if(CalendarData.month > 1):
                    CalendarData.month -= 1
                else:
                    CalendarData.month = 12
                    CalendarData.year -= 1
                sm.current = 'Calendar1'
        def downPressed(instance, value):
            if value == 'down':
                if(CalendarData.month > 11):
                    CalendarData.month += 1
                else:
                    CalendarData.month = 1
                    CalendarData.year += 1
                sm.current = 'Calendar1'
        with sc.canvas:      # set background
            Color(.9, .9, .9)
            Rectangle(pos_hint={'x':.5, 'y':.5}, size=(100000, 100000))

        btns = GridLayout(cols = 1, rows = 2)
        up = Button(text = '[color=000000]PREV[/color]', markup = True, background_color = (1,1,1,0))
        btns.add_widget(up)
        up.bind(state=upPressed)
        down = Button(text = '[color=000000]NEXT[/color]', markup = True, background_color = (1,1,1,0))
        btns.add_widget(down)
        down.bind(state=downPressed)

        year = CalendarData.year
        month = CalendarData.month
        monthName = CalendarData.monthName
        print(str(year) + '   '+ str(month))

        sc.add_widget(Label(text = ''))
        sc.add_widget(Label(text = ''))
        sc.add_widget(Label(text = ''))
        lb = Label(text = '[color=000000]' + str(monthName) + ' Caldendar '+ str(year) + '[/color]', font_size = '40sp', markup = True)
        def update(dt):
            year = CalendarData.year
            month = CalendarData.month
            monthName = CalendarData.monthName
            print(CalendarData.monthName)
            lb = Label(text = '[color=000000]' + str(monthName) + ' Caldendar '+ str(year) + '[/color]', font_size = '40sp', markup = True)
        sc.add_widget(lb)
        Clock.schedule_interval(update, 0.1)
        sc.add_widget(Label(text = ''))
        sc.add_widget(Label(text = ''))
        sc.add_widget(btns)
        ls = []
        dotwls = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] #day of the week list
        for x in range(7):
            ls.append(dotwls[x])
        for x in range(CalendarData.firstDayOfMonth(year, month)):
            ls.append('')
        for x in range(CalendarData.monthLength(year, month)):
            ls.append(x + 1)
        for x in ls:
            sc.add_widget(Label(text = '[color=000000]' + str(x) + '[/color]', markup = True))
        scrn = FloatLayout()
        scrn.add_widget(sc)
        self.add_widget(scrn)

class Calendar1(Screen):
    def __init__(self, **kwargs):
        super(Calendar1, self).__init__(**kwargs)
        sc = GridLayout(cols = 7, rows = 7)
        def colorSelector(decValue):  #255,255,255 -> 1,1,1,1 (rgb -> rgba)
            result = []
            for x in decValue:
                result.append(x / 255)
            result.append(1)
            return result
            return None
        def upPressed(instance, value):
            if value == 'down':
                if(CalendarData.month > 1):
                    CalendarData.month -= 1
                else:
                    CalendarData.month = 12
                    CalendarData.year -= 1
                sm.current = 'Calendar'
        def downPressed(instance, value):
            if value == 'down':
                if(CalendarData.month > 11):
                    CalendarData.month += 1
                else:
                    CalendarData.month = 1
                    CalendarData.year += 1
                sm.current = 'Calendar'
        with sc.canvas:      # set background
            Color(.9, .9, .9)
            Rectangle(pos_hint={'x':.5, 'y':.5}, size=(100000, 100000))

        btns = GridLayout(cols = 1, rows = 2)
        up = Button(text = '[color=000000]PREV[/color]', markup = True, background_color = (1,1,1,0))
        btns.add_widget(up)
        up.bind(state=upPressed)
        down = Button(text = '[color=000000]NEXT[/color]', markup = True, background_color = (1,1,1,0))
        btns.add_widget(down)
        down.bind(state=downPressed)

        year = CalendarData.year
        month = CalendarData.month
        monthName = CalendarData.monthName

        sc.add_widget(Label(text = ''))
        sc.add_widget(Label(text = ''))
        sc.add_widget(Label(text = ''))
        sc.add_widget(Label(text = '[color=000000]' + str(monthName) + ' '+ str(year) + '[/color]', font_size = '40sp', markup = True))
        sc.add_widget(Label(text = ''))
        sc.add_widget(Label(text = ''))
        sc.add_widget(btns)
        ls = []
        dotwls = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] #day of the week list
        for x in range(7):
            ls.append(dotwls[x])
        for x in range(CalendarData.firstDayOfMonth(year, month)):
            ls.append('')
        for x in range(CalendarData.monthLength(year, month)):
            ls.append(x + 1)
        for x in ls:
            sc.add_widget(Label(text = '[color=000000]' + str(x) + '[/color]', markup = True))
        scrn = FloatLayout()
        scrn.add_widget(sc)
        self.add_widget(scrn)

class Calendarsc(Screen):
    def __init__(self, **kwargs):
        super(Calendar, self).__init__(**kwargs)
        sc = FloatLayout()
        def colorSelector(decValue):
            result = []
            for x in decValue:
                result.append(x / 255)
            result.append(1)
            return result
        def dCallback(instance, value):
            if(value == 'down'):
                sm.current = 'Dashboard'
        def weekPressed(instance, value):
              if(value == 'down'):
                  sm.current = 'Week'
        def monthPressed(instance, value):
              if(value == 'down'):
                  sm.current = 'Month'
        with sc.canvas:       # set background
            Color(.9, .9, .9)
            Rectangle(pos_hint={'x':.5, 'y':.5}, size=(100000, 100000))

        # Title
        title = Label(pos_hint={'x':0, 'y':.4}, text = '[color=0055ff][font=5thgradecursive]Calendar[/font][/color]', font_size='60sp', markup = True)
        sc.add_widget(title)
        # Week button
        week = Button(pos_hint={'x':0, 'y':.6501}, size_hint=(.24,.12), text = 'Week', font_size='30sp', background_color= colorSelector([160,32,240]), markup = True)
        week.bind(state=dCallback)
        sc.add_widget(week)
        week.bind(state=weekPressed)
        # Month button
        month = Button(pos_hint={'x':0, 'y':.375}, size_hint=(.24,.12), text = 'Month', font_size='30sp', background_color = colorSelector([0, 255, 0]), markup = True)
        sc.add_widget(month)
        month.bind(state=monthPressed)
        # Back button
        back = Button(pos_hint={'x':0, 'y':0.9}, size_hint=(.24,.12), text = 'Back', font_size='30sp', background_color = colorSelector([0, 0, 0]), markup = True)
        sc.add_widget(back)
        back.bind(state=dCallback)
        self.add_widget(sc)


class Settings(Screen):
    def __init__(self, **kwargs):
        super(Settings, self).__init__(**kwargs)
        sc = FloatLayout()
        def colorSelector(decValue):
            result = []
            for x in decValue:
                result.append(x / 255)
            result.append(1)
            return result
        def dCallback(instance, value):
            if(value == 'down'):
                sm.current = 'Dashboard'
        def holidayPressed(instance, value):
            if(value == 'down'):
                sm.current = 'Holiday'
        def classesPressed(instance, value):
            if(value == 'down'):
                sm.current = 'Classes'
        def accountPressed(instance, value):
            if(value == 'down'):
                sm.current = 'Account'
        with sc.canvas:       # set background
            Color(.9, .9, .9)
            Rectangle(pos_hint={'x':.5, 'y':.5}, size=(100000, 100000))

        # Title
        title = Label(pos_hint={'x':0, 'y':.4}, text = '[color=0055ff][font=5thgradecursive]Settings[/font][/color]', font_size='60sp', markup = True)
        sc.add_widget(title)
        # Classes button
        classes = Button(pos_hint={'x':0, 'y':.6501}, size_hint=(.24,.12), text = 'Class', font_size='30sp', background_color= colorSelector([160,32,240]), markup = True)
        classes.bind(state=dCallback)
        sc.add_widget(classes)
        # Holiday button
        holiday = Button(pos_hint={'x':0, 'y':.375}, size_hint=(.24,.12), text = 'Holiday', font_size='30sp', background_color = colorSelector([0, 255, 0]), markup = True)
        sc.add_widget(holiday)
        holiday.bind(state=holidayPressed)
        # Account button
        account = Button(pos_hint={'x':0, 'y':.1}, size_hint=(.24,.12), text = 'Account', font_size='30sp', background_color = colorSelector([255, 10, 10]), markup = True)
        sc.add_widget(account)
        account.bind(state=accountPressed)
        # Back button
        back = Button(pos_hint={'x':0, 'y':0.9}, size_hint=(.24,.12), text = 'Back', font_size='30sp', background_color = colorSelector([0, 0, 0]), markup = True)
        sc.add_widget(back)
        back.bind(state=dCallback)

        self.add_widget(sc)


class Dashboard(Screen):
    def __init__(self, **kwargs):
        print('zhe li')
        super(Dashboard, self).__init__(**kwargs)
        sc = FloatLayout()
        def colorSelector(decValue):  #255,255,255 -> 1,1,1,1 (rgb -> rgba)
            result = []
            for x in decValue:
                result.append(x / 255)
            result.append(1)
            return result
        def assPressed(instance, value):
            if(value == 'down'):
                sm.current = 'Assignments'
        def calPressed(instance, value):
            if(value == 'down'):
                sm.current = 'Calendar'
        def settingsPressed(instance, value):
            if(value == 'down'):
                sm.current = 'Settings'
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


class Assignments(Screen):
    def __init__(self, **kwargs):
        super(Assignments, self).__init__(**kwargs)
        sc = FloatLayout()
        def colorSelector(decValue):
            result = []
            for x in decValue:
                result.append(x / 255)
            result.append(1)
            return result
        def dCallback(instance, value):
            if(value == 'down'):
                sm.current = 'Dashboard'
        def hwPressed(instance, value):
            if(value == 'down'):
                sm.current = 'Homework'
        def testsPressed(instance, value):
            if(value == 'down'):
                sm.current = 'Tests'
        def eventsPressed(instance, value):
            if(value == 'down'):
                sm.current = 'Events'
        with self.canvas:       # set background
            Color(.9, .9, .9)
            Rectangle(pos_hint={'x':.5, 'y':.5}, size=(100000, 100000))
        with self.canvas:
            # Add a red color
            Color(1, 0, 0)
            # Add a rectangle
            Rectangle(pos=(0, 600), size=(1500, 2))

        # Title
        title = Label(pos_hint={'x':0, 'y':.4}, text = '[color=0055ff][font=5thgradecursive]Assignments[/font][/color]', font_size='60sp', markup = True)
        self.add_widget(title)
        # Homework button
        homework = Button(pos_hint={'x':0, 'y':.6501}, size_hint=(.24,.12), text = 'Homework', font_size='30sp', background_color= colorSelector([160,32,240]), markup = True)
        homework.bind(state=dCallback)
        self.add_widget(homework)
        # Tests button
        tests = Button(pos_hint={'x':0, 'y':.375}, size_hint=(.24,.12), text = 'Tests', font_size='30sp', background_color = colorSelector([0, 255, 0]), markup = True)
        tests.bind(state=testsPressed)
        self.add_widget(tests)
        # Events button
        events = Button(pos_hint={'x':0, 'y':.1}, size_hint=(.24,.12), text = 'Events', font_size='30sp', background_color = colorSelector([255, 10, 10]), markup = True)
        events.bind(state=eventsPressed)
        self.add_widget(events)
        # Back button
        back = Button(pos_hint={'x':0, 'y':0.9}, size_hint=(.24,.12), text = 'Back', font_size='30sp', background_color = colorSelector([0, 0, 0]), markup = True)
        self.add_widget(back)
        back.bind(state=dCallback)
        self.add_widget(sc)

#class Timer(Screen):
  #def listening(thisWord):
	#signal = raw_input(thisWord)
	#return signal
	#t = threading.Timer(30.0, listening(thisWord)
	#t.start()
#
class StartScreen(Screen):
    pass

sm = ScreenManager(transition=SlideTransition())
sm.add_widget(StartScreen(name='start'))
sm.add_widget(Dashboard(name='Dashboard'))
sm.add_widget(Settings(name = 'Settings'))
sm.add_widget(Calendar(name = 'Calendar'))
sm.add_widget(Calendar1(name = 'Calendar1'))
sm.add_widget(Assignments(name = 'Assignments'))




class SimpleKivy(App):
    def build(self):
        return sm


if __name__ == "__main__":
    SimpleKivy().run()
