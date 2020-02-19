from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class WindowManager(ScreenManager):
    pass

class LoginScreen(Screen):
    def login(self):
        print(self.ids['passw'].text)
        self.manager.current = 'home'

class HomeScreen(Screen):
    pass

kv = Builder.load_file('erp.kv')

class ErpApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    ErpApp().run()