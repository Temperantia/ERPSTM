from kivy.uix.button import Button
from frontend.widgets.title import standardTitle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from frontend.globals import sm


class Home(Screen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        b = BoxLayout(orientation='vertical')
        b.padding = [10, 10, 10, 10]
        b.pos = (0, 0)
        b.spacing = 40
        b.size_hint = (0.5, 1)
        b.pos_hint = {'x': 0.25}

        title = standardTitle('Bienvenue')
        b.add_widget(title)

        l = Label()
        b.add_widget(l)

        buttnLogin = Button()
        buttnLogin.text = 'Demandes en cours'
        buttnLogin.on_press = self.goToRequests
        b.add_widget(buttnLogin)
        self.add_widget(b)

    def goToRequests(self):
        sm.current = 'requests'