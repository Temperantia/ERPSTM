from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from functools import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager


def standardTextField(text):
    t = TextInput()
    t.hint_text = text
    t.size_hint = (0.4, 1)
    t.font_size = 25
    t.focus = True
    t.size_hint_max_y = 40
    t.multiline = False
    return t


class Login(Screen):
    nom = None
    mdp = None

    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        b = BoxLayout(orientation='vertical')
        b.padding = [10, 10, 10, 10]
        b.pos = (0, 0)
        b.spacing = 40

        self.nom = standardTextField("Nom")
        self.mdp = standardTextField("Mot de passe")
        self.mdp.password = True
        b.add_widget(self.nom)
        b.add_widget(self.mdp)

        btn = Button(text="Valider")
        btn.size_hint = (.4, 0.1)
        btn.on_press = self.validating
        l = Label(text="")

        b.add_widget(btn)
        b.add_widget(l)
        self.add_widget(b)

    def validating(self):
        self.getFields()
        self.clearFields()

    def getFields(self):
        nom = self.nom.text
        mdp = self.mdp.text
        print(nom, mdp)
        return (nom, mdp)

    def clearFields(self):
        self.nom.text = ""
        self.mdp.text = ""


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        login = Login(name='login')
        sm.add_widget(login)

        return sm


MyApp().run()
