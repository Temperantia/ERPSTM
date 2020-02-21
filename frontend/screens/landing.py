from kivy.uix.button import Button
from frontend.widgets.title import standardTitle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from frontend.globals import sm


class PickRegisterOrLogin(Screen):
    def __init__(self, **kwargs):
        super(PickRegisterOrLogin, self).__init__(**kwargs)
        b = BoxLayout(orientation='vertical')
        b.padding = [10, 10, 10, 10]
        b.pos = (0, 0)
        b.spacing = 40
        b.size_hint = (0.5, 1)
        b.pos_hint = {'x': 0.25}

        title = standardTitle('Identifiez-vous')
        b.add_widget(title)

        buttnLogin = Button()
        buttnLogin.text = 'J\'ai déjà un compte'
        buttnLogin.on_press = self.goToLoginScreen

        buttnRegister = Button()
        buttnRegister.text = 'Je n\'ai pas de compte'
        buttnRegister.on_press = self.goToRegisterSreen

        b.add_widget(buttnLogin)
        b.add_widget(buttnRegister)

        l = Label()
        b.add_widget(l)
        self.add_widget(b)

    def goToLoginScreen(self):
        sm.current = 'login'

    def goToRegisterSreen(self):
        sm.current = 'register'
