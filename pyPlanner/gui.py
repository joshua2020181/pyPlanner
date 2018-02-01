# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 19:01:36 2017

@author: joshua_cheng + conner_morgan
"""
from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.graphics import *
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, WipeTransition
from kivy.properties import StringProperty
from kivy.clock import Clock
import time
import main
from main import *
import pickle


CalendarData.year = DateTime.year
CalendarData.month = DateTime.month
year = CalendarData.year
month = CalendarData.month
monthName = CalendarData.monthName

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


def colorSelector(decValue):
    result = []
    for x in decValue:
        result.append(x / 255)
    result.append(1)
    return result

def spacer(sc):
    sc.add_widget(Label(text = ''))

class User(object):
        name = ''
        schoolYearName = ''
        schoolYear = ''
        holidayNames = ['']
        holidays = [] #dates ex: 11/10/17
        nBlocks = 8
        nBlocksPerDay = 4
        dayRotation = 2 #how many day rotation scheduel (2)
        nClasses = 0 #number of classes
        classes = [''] #list of classes (nClasses long)
        classLength = [] #length of that class (minutes) (nClasses long)
        tasks = []
        def __init__(self, name, schoolYearName='', schoolYear=['9/1/17', '6/1/18'], holidayNames=[''], holidays=[], nBlocks=8, dayRotation=2, nBlocksPerDay=nBlocks/dayRotation, classes=[''], nClasses=len(classes), classLength=[]):
            self.name = name
            self.schoolYearName = schoolYearName
            self.schoolYear = schoolYear
            self.holidayNames = holidayNames
            self.holidays = holidays #dates ex: 11/10/17
            self.nBlocks = nBlocks
            self.nBlocksPerDay = nBlocksPerDay
            self.dayRotation = dayRotation #how many day rotation scheduel (2)
            self.nClasses = nClasses #number of classes
            self.classes = classes #list of classes (nClasses long) (subjects)
            self.classLength = classLength #length of that class (minutes) (nClasses long)

user1 = User('Joshua', 'Sophmore Year', ['9/1/17', '6/1/18'], classes=['Math', 'English', 'Science', 'History', 'Art', 'Language'], nClasses=6)

class Task(object):
    name = "Untitled"
    description = "None"
    subject = ""
    dueDate = ["Month", "Day", "Year"]
    taskType = ''
    def __init__(self, name, description='None', subject='', dueDate=["Month", "Day", "Year"], taskType='other'):
        self.name = name
        self.description = description
        self.subject = subject
        self.dueDate = dueDate
        self.taskType = taskType

user1.tasks.append(Task('Khan Academy', '3 videos'))

class Calendar(Screen):
    def __init__(self, **kwargs):
        super(Calendar, self).__init__(**kwargs)
        sc = GridLayout(cols = 7, rows = 8) #7,7
        def upPressed(instance, value):
            if value == 'down':
                # self.manager.transition.direction = 'right'
                if(CalendarData.month > 1):
                    CalendarData.month -= 1
                else:
                    CalendarData.month = 12
                    CalendarData.year -= 1
                self.manager.get_screen('Calendar1').lb.text = '[color=000000]' + str(CalendarData.monthName(CalendarData.month)) + " " + str(CalendarData.year) + '[/color]'
                self.manager.get_screen('Calendar').lb.text = '[color=000000]' + str(CalendarData.monthName(CalendarData.month)) + " " + str(CalendarData.year) + '[/color]'
                ls = []
                dotwls = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] #day of the week list
                for x in range(7):
                    ls.append(dotwls[x])
                for x in range(CalendarData.firstDayOfMonth(CalendarData.year, CalendarData.month)):
                    ls.append('')
                for x in range(CalendarData.monthLength(CalendarData.year, CalendarData.month)):
                    ls.append(x + 1)
                for x in range(42):
                    ls.append('')
                for x in range(len(self.lsOfWidgets)):
                    self.manager.get_screen('Calendar').lsOfWidgets[x].text = text = '[color=000000]' + str(ls[x]) + '[/color]'
                    self.manager.get_screen('Calendar1').lsOfWidgets[x].text = text = '[color=000000]' + str(ls[x]) + '[/color]'
                sm.current = 'Calendar1'
        def downPressed(instance, value):
            # self.manager.transition.direction = 'left'
            if value == 'down':
                if(CalendarData.month <= 11):
                    CalendarData.month += 1
                else:
                    CalendarData.month = 1
                    CalendarData.year += 1
                self.manager.get_screen('Calendar').lb.text = '[color=000000]' + str(CalendarData.monthName(CalendarData.month)) + " " + str(CalendarData.year) + '[/color]'
                self.manager.get_screen('Calendar1').lb.text = '[color=000000]' + str(CalendarData.monthName(CalendarData.month)) + " " + str(CalendarData.year) + '[/color]'
                ls = []
                dotwls = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] #day of the week list
                for x in range(7):
                    ls.append(dotwls[x])
                for x in range(CalendarData.firstDayOfMonth(CalendarData.year, CalendarData.month)):
                    ls.append('')
                for x in range(CalendarData.monthLength(CalendarData.year, CalendarData.month)):
                    ls.append(x + 1)
                for x in range(42):
                    ls.append('')
                for x in range(len(self.lsOfWidgets)):
                    self.manager.get_screen('Calendar').lsOfWidgets[x].text = text = '[color=000000]' + str(ls[x]) + '[/color]'
                    self.manager.get_screen('Calendar1').lsOfWidgets[x].text = text = '[color=000000]' + str(ls[x]) + '[/color]'
                sm.current = 'Calendar1'
        def backPressed(instance, value):
            if(value == 'down'):
                sm.current = 'Dashboard'
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
        back = GridLayout(cols = 1, rows = 2)
        backbtn = Button(text = '[color=000000]' + 'Back' + '[/color]', font_size = '20sp', markup = True, background_color = (1,1,1,0))
        backbtn.bind(state=backPressed)
        back.add_widget(backbtn)
        spacer(back)
        sc.add_widget(back)

        spacer(sc)
        spacer(sc)

        self.lb = Label(id = 'lbid', text = '[color=000000]' + str(CalendarData.monthName(CalendarData.month)) + " " + str(CalendarData.year) + '[/color]', font_size = '40sp', markup = True)
        sc.add_widget(self.lb)
        spacer(sc)
        spacer(sc)
        sc.add_widget(btns)
        ls = []
        self.lsOfWidgets = []
        dotwls = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] #day of the week list
        for x in range(7):
            ls.append(dotwls[x])
        for x in range(CalendarData.firstDayOfMonth(CalendarData.year, CalendarData.month)):
            ls.append('')
        for x in range(CalendarData.monthLength(CalendarData.year, CalendarData.month)):
            ls.append(x + 1)
        for x in range(len(ls)):
            self.lsOfWidgets.append(Label(text = '[color=000000]' + str(ls[x]) + '[/color]', markup = True))
            sc.add_widget(self.lsOfWidgets[x])
        self.lsOfWidgets.append(Label(text = ''))
        self.add_widget(sc)
        cal = sc

class Calendar1(Screen):
    def __init__(self, **kwargs):
        super(Calendar1, self).__init__(**kwargs)
        sc = GridLayout(cols = 7, rows = 8)
        def colorSelector(decValue):  #255,255,255 -> 1,1,1,1 (rgb -> rgba)
            result = []
            for x in decValue:
                result.append(x / 255)
            result.append(1)
            return result
            return None
        def upPressed(instance, value):
            if value == 'down':
                # self.manager.transition.direction = 'right'
                if(CalendarData.month > 1):
                    CalendarData.month -= 1
                else:
                    CalendarData.month = 12
                    CalendarData.year -= 1
                self.manager.get_screen('Calendar1').lb.text = '[color=000000]' + str(CalendarData.monthName(CalendarData.month)) + " " + str(CalendarData.year) + '[/color]'
                self.manager.get_screen('Calendar').lb.text = '[color=000000]' + str(CalendarData.monthName(CalendarData.month)) + " " + str(CalendarData.year) + '[/color]'
                ls = []
                dotwls = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] #day of the week list
                for x in range(7):
                    ls.append(dotwls[x])
                for x in range(CalendarData.firstDayOfMonth(CalendarData.year, CalendarData.month)):
                    ls.append('')
                for x in range(CalendarData.monthLength(CalendarData.year, CalendarData.month)):
                    ls.append(x + 1)
                for x in range(42):
                    ls.append('')
                for x in range(len(self.lsOfWidgets)):
                    self.manager.get_screen('Calendar1').lsOfWidgets[x].text = text = '[color=000000]' + str(ls[x]) + '[/color]'
                    self.manager.get_screen('Calendar').lsOfWidgets[x].text = text = '[color=000000]' + str(ls[x]) + '[/color]'
                sm.current = 'Calendar'
        def downPressed(instance, value):
            if value == 'down':
                # self.manager.transition.direction = 'left'
                if(CalendarData.month <= 11):
                    CalendarData.month += 1
                else:
                    CalendarData.month = 1
                    CalendarData.year += 1
                self.manager.get_screen('Calendar').lb.text = '[color=000000]' + str(CalendarData.monthName(CalendarData.month)) + " " + str(CalendarData.year) + '[/color]'
                self.manager.get_screen('Calendar1').lb.text = '[color=000000]' + str(CalendarData.monthName(CalendarData.month)) + " " + str(CalendarData.year) + '[/color]'
                ls = []
                dotwls = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] #day of the week list
                for x in range(7):
                    ls.append(dotwls[x])
                for x in range(CalendarData.firstDayOfMonth(CalendarData.year, CalendarData.month)):
                    ls.append('')
                for x in range(CalendarData.monthLength(CalendarData.year, CalendarData.month)):
                    ls.append(x + 1)
                for x in range(42):
                    ls.append('')
                for x in range(len(self.lsOfWidgets)):
                    self.manager.get_screen('Calendar').lsOfWidgets[x].text = text = '[color=000000]' + str(ls[x]) + '[/color]'
                    self.manager.get_screen('Calendar1').lsOfWidgets[x].text = text = '[color=000000]' + str(ls[x]) + '[/color]'
                sm.current = 'Calendar'
        def backPressed(instance, value):
            if(value == 'down'):
                sm.current = 'Dashboard'
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
        back = GridLayout(cols = 1, rows = 2)
        backbtn = Button(text = '[color=000000]' + 'Back' + '[/color]', font_size = '20sp', markup = True, background_color = (1,1,1,0))
        backbtn.bind(state=backPressed)
        back.add_widget(backbtn)
        spacer(back)
        sc.add_widget(back)
        spacer(sc)
        spacer(sc)

        self.lb = Label(id = 'lbid', text = '[color=000000]' + str(CalendarData.monthName(CalendarData.month)) + " " + str(CalendarData.year) + '[/color]', font_size = '40sp', markup = True)
        sc.add_widget(self.lb)
        spacer(sc)
        spacer(sc)
        sc.add_widget(btns)
        ls = []
        self.lsOfWidgets = []
        dotwls = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] #day of the week list
        for x in range(7):
            ls.append(dotwls[x])
        for x in range(CalendarData.firstDayOfMonth(CalendarData.year, CalendarData.month)):
            ls.append('')
        for x in range(CalendarData.monthLength(CalendarData.year, CalendarData.month)):
            ls.append(x + 1)
        for x in range(len(ls)):
            self.lsOfWidgets.append(Label(text = '[color=000000]' + str(ls[x]) + '[/color]', markup = True))
            sc.add_widget(self.lsOfWidgets[x])
        self.lsOfWidgets.append(Label(text = ''))
        scrn = FloatLayout()
        scrn.add_widget(sc)
        self.add_widget(scrn)

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

class AddTask(Screen):
    def __init__(self, **kwargs):
        super(AddTask, self).__init__(**kwargs)
        sc = FloatLayout()
        self.taskName = ''
        self.taskDescription = ''
        self.taskDueDate = ['']
        self.taskSubject = ''

        with self.canvas:       # set background
            Color(.9, .9, .9)
            Rectangle(pos_hint={'x':.5, 'y':.5}, size=(100000, 100000))

        def cancelCallback(instance, value):
            sm.current = 'Assignments'
        def nameEntered(instance, value):
            print(self.taskName)
            self.taskName = value
        def descEntered(instance, value):
            print(self.taskDescription)
            self.taskDescription = value
        def datePressed(instance):
            pass
        def addPressed(instance, value):
            if value == 'down':
                if 'Select' in self.manager.get_screen('AddTask').selectSubject.text:
                    print('Error: Please choose a subject')
                else:
                    self.taskSubject = self.manager.get_screen('AddTask').selectSubject.text[14:-8]
                    print(self.taskName)
                    createdTask = Task(self.taskName, self.taskDescription, self.taskSubject, ['10','1','17'])
                    user1.tasks.append(createdTask)
                    user1.tasks.append(Task('test','test1'))
                    print(self.manager.get_screen('Assignments').templs)

                    temptempls = []
                    for x in range(len(user1.tasks)):
                        print(x)
                        print(user1.tasks[x].name)
                        temptempls.append(user1.tasks[x].name)
                        temptempls.append(user1.tasks[x].description)
                    for x in range(len(temptempls)):
                        self.manager.get_screen('Assignments').templs[x].text = text = '[color=000000]' + str(temptempls[x]) + '[/color]'

                    sm.current='Assignments'


        grid = GridLayout(cols = 2, rows = 5, pos_hint={'x':.25, 'y':.25}, size_hint=(.5,.5))

        grid.add_widget(Label(text = '[color=000000]Name: [/color]', markup=True))

        nameInput = TextInput(multiline=False)
        nameInput.bind(text=nameEntered)
        grid.add_widget(nameInput)

        grid.add_widget(Label(text = '[color=000000]Description: [/color]', markup=True))
        descInput = TextInput(multiline=False)
        descInput.bind(text=descEntered)
        grid.add_widget(descInput)

        grid.add_widget(Label(text = '[color=000000]Subject: [/color]', markup=True))


        # lsOfTasks = []
        # lsOfTasks.append(Task('Khan Academy', '3 videos'))
        # with open('taskData.pkl', 'wb') as output:
        #     pickle.dump(lsOfTasks, output, pickle.HIGHEST_PROTOCOL)



        self.selectSubject = Button(text='[color=000000]Select[/color]', markup=True, size_hint=(.2,.2))

        subjectDropDown = DropDown(size_hint=(.0001,.01))


        for i in range(user1.nClasses):
            print('here')
            btn = Button(text='[color=000000]' + user1.classes[i] + '[/color]', markup=True, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: subjectDropDown.select(btn.text))
            subjectDropDown.add_widget(btn)
        self.selectSubject.bind(on_release=subjectDropDown.open)
        subjectDropDown.bind(on_select=lambda instance, x: setattr(self.selectSubject, 'text', x))

        grid.add_widget(self.selectSubject)
        self.add_widget(subjectDropDown)

        grid.add_widget(Label(text='[color=000000]Due Date: [/color]', markup=True))

        dateBtn = Button(text='[color=000000]Select[/color]', markup=True)
        dateDropDown = DropDown(max_height=210, size_hint=(.001,.001))
        dateDropDown.container.cols = 7

        ls = []
        self.lsOfWidgets = []
        dotwls = ['S', 'M', 'T', 'W', 'T', 'F', 'S'] #day of the week list

        m = CalendarData.month
        y = CalendarData.year

        asdf = Label(text = 'hello')
        # with asdf.canvas:
        #     Color(0,0,0)
        #     Rectangle(pos=asdf.)

        # grid.add_widget(asdf)

        for i in range(12):
            ls = []
            self.lsOfWidgets = []
            for x in range(3):
                spacer(dateDropDown)
            title = Label(text = '[color=000000]' + CalendarData.monthName(m) + ' ' + str(y) + '[/color]', markup=True, size_hint_y=None, height=30)
            dateDropDown.add_widget(title)
            for x in range(3):
                spacer(dateDropDown)
            for x in range(7):
                ls.append(dotwls[x])
            for x in range(CalendarData.firstDayOfMonth(y, m)):
                ls.append('')
            for x in range(CalendarData.monthLength(y, m)):
                ls.append(x + 1)
            for x in range(len(ls)):
                if(type(ls[x])==int):
                    btn = Button(text = '[color=000000]' + str(ls[x]) + '[/color]', markup=True, size_hint_y=None, height=30)
                    self.lsOfWidgets.append(Button(text = '[color=000000]' + str(ls[x]) + '[/color]', markup=True, size_hint_y=None, height=30))
                    self.lsOfWidgets[x].bind(on_release=lambda btn: dateDropDown.select(btn.text))
                else:
                    self.lsOfWidgets.append(Button(text = '[color=000000]' + str(ls[x]) + '[/color]', markup=True, size_hint_y=None, height=30))
                dateDropDown.add_widget(self.lsOfWidgets[x])
            for x in range(49 - len(ls)):
                spacer(dateDropDown)
            m += 1
            if(m > 12):
                y += 1
                m = 1

        # for i in range(56): #rows
        #     dbtn = Button(text='[color=000000]hello[/color]', markup=True, size_hint_y=None, height=30)
        #     dbtn.bind(on_release=lambda btn: dateDropDown.select(dbtn.text))
        #     dateDropDown.add_widget(dbtn)
        dateBtn.bind(on_release=dateDropDown.open)
        dateDropDown.bind(on_select=lambda instance, x: setattr(dateBtn, 'text', '[color=000000]' + CalendarData.monthName(m) + ' ' + x[14:-8] + ', ' + str(y) + '[/color]'))
        grid.add_widget(dateBtn)
        grid.add_widget(dateDropDown)

        self.add_widget(grid)
        title = Label(pos_hint={'x':0, 'y':.4}, text = '[color=0055ff]Add Task[/color]', font_size='60sp', markup = True)
        self.add_widget(title)
        cancel = Button(pos_hint={'x':0, 'y':0.925}, size_hint=(.15,.075), text = 'Cancel', font_size='15sp', background_color = colorSelector([0, 0, 0]), markup = True)
        self.add_widget(cancel)
        cancel.bind(state=cancelCallback)
        add = Button(pos_hint={'x':0.85, 'y':0.925}, size_hint=(.15,.075), text = 'add', font_size='15sp', background_color = colorSelector([0, 0, 0]), markup = True)
        self.add_widget(add)
        add.bind(state=addPressed)

class Assignments(Screen):
    def __init__(self, **kwargs):
        super(Assignments, self).__init__(**kwargs)
        sc = FloatLayout()
        def dCallback(instance, value):
            if(value == 'down'):
                sm.current = 'Dashboard'
        def aCallback(instance, value): #add assignment button
            if(value == 'down'):
                sm.current = 'AddTask'
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
        homework = Button(pos_hint={'x':0, 'y':.7}, size_hint=(.24,.12), text = 'Homework', font_size='30sp', background_color= colorSelector([160,32,240]), markup = True)
        homework.bind(state=dCallback)
        self.add_widget(homework)
        # Tests button
        tests = Button(pos_hint={'x':0, 'y':.5}, size_hint=(.24,.12), text = 'Tests', font_size='30sp', background_color = colorSelector([0, 255, 0]), markup = True)
        tests.bind(state=testsPressed)
        self.add_widget(tests)
        # Events button
        events = Button(pos_hint={'x':0, 'y':.3}, size_hint=(.24,.12), text = 'Events', font_size='30sp', background_color = colorSelector([255, 10, 10]), markup = True)
        events.bind(state=eventsPressed)
        self.add_widget(events)

        other = Button(pos_hint={'x':0, 'y':.1}, size_hint=(.24,.12), text = 'Other', font_size='30sp', background_color = colorSelector([10, 10, 255]), markup = True)
        self.add_widget(other)
        # Back button
        back = Button(pos_hint={'x':0, 'y':0.88}, size_hint=(.24,.12), text = 'Back', font_size='30sp', background_color = colorSelector([0, 0, 0]), markup = True)
        self.add_widget(back)
        back.bind(state=dCallback)

        add = Button(pos_hint={'x':.88, 'y':.7}, size_hint=(.12,.12), text = '+', font_size='50sp', background_color = colorSelector([0, 0, 0]), markup = True)
        self.add_widget(add)
        add.bind(state=aCallback)

        btnLayout = GridLayout(cols = 1, rows = 10, pos_hint={'x':.24, 'y':.1}, size_hint=(.1,.7))

        self.btnls = []
        for x in range(len(user1.tasks)):
            self.btnls.append(Button()) #this task is completed button
            btnLayout.add_widget(self.btnls[x])
        for x in range(10 - len(user1.tasks)):
            btnLayout.add_widget(Label())
        self.add_widget(btnLayout)

        lsLayout = GridLayout(cols = 2, rows = 10, pos_hint={'x':.34, 'y':.1}, size_hint=(.5,.7))

        # lsOfTasks = []
        # lsOfTasks.append(Task('hello', 'description'))
        # lsOfTasks.append(Task('hello1', 'description1'))
        # with open('taskData.pkl', 'wb') as output:
        #     pickle.dump(lsOfTasks, output, pickle.HIGHEST_PROTOCOL)

        self.templs = []
        for x in range(len(user1.tasks)):
            self.templs.append(Label(text = '[color=000000]' + user1.tasks[x].name + '[/color]', font_size='15sp', markup = True))
            self.templs.append(Label(text = '[color=000000]' + user1.tasks[x].description + '[/color]', font_size='15sp', markup = True))
        for i in range(20 - (2 * len(self.templs))):
            self.templs.append(Label(text = '[color=000000]' + '' + '[/color]', font_size='15sp', markup = True))
        for x in range(len(self.templs)):
            lsLayout.add_widget(self.templs[x])

        self.add_widget(lsLayout)


class StartScreen(Screen):
    pass

sm = ScreenManager(transition=SlideTransition())
sm.add_widget(AddTask(name = 'AddTask'))
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
