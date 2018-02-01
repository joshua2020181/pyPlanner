# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.screenmanager import Screen
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# from kivy.properties import ObjectProperty, StringProperty
# from kivy.clock import Clock
# import time
# from datetime import datetime
#
# Builder.load_string('''
# <MainScreen>:
#     name: 'main'
#     the_time: _id_lbl_time
#     BoxLayout:
#         orientation: 'vertical'
#         Label:
#             id: _id_lbl_time
#             text: 'Time'
#             font_size: 60
#  ''')
#
# asdf = '''
# Label:
#     text: 'Hello'
# '''
#
# class sc(Screen):
#     def __init__(self, **kwargs):
#         super(sc, self).__init__(**kwargs)
#         box = GridLayout(cols = 2, rows = 2)
#         box.add_widget(Label(text = 'here'))
#         box.add_widget(Builder.load_string(asdf))
#         self.add_widget(box)
#
# class MainScreen(Screen):
#     def update_time(self, sec):
#         MyTime = time.strftime("%H:%M:%S")
#         self.the_time.text = MyTime
#
#
# class ScreenManagerApp(App):
#
#     def build(self):
#         #self.main_screen = MainScreen()
#         self.sc_sc = sc()
#         #return self.main_screen
#         return sc(name = 'asdf')
#
#     # def on_start(self):
#     #     Clock.schedule_interval(self.main_screen.update_time, 1)
#
# ScreenManagerApp().run()


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

Builder.load_string('''
<MainScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: 'Goto strategy'
            on_press: root.manager.current = 'strategy'
        Button:
            text: 'Set text'
            on_press: root.SetText()

<StrategyScreen>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: root.labelText
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'main'
''')

class MainScreen(Screen):
    def SetText(self):
        text = 'Total=' + str(17*21)
        self.manager.get_screen('strategy').labelText = text

class StrategyScreen(Screen):
    labelText = StringProperty('My label')

class TestApp(App):
    def build(self):
        # Create the screen manager
        screenManager = ScreenManager()
        screenManager.add_widget(MainScreen(name='main'))
        screenManager.add_widget(StrategyScreen(name='strategy'))
        return screenManager

if __name__ == '__main__':
    TestApp().run()
