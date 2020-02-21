from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from frontend.widgets.title import standardTitle
from frontend.widgets.text_field import standardTextField
from kivy.uix.button import Button
from kivy.uix.label import Label
from frontend.sm import sm
from frontend.globals import user
from backend.login import login_user


class Login(Screen):
    nom = None
    mdp = None
    connexionRefused = None

    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        b = BoxLayout(orientation='vertical')
        b.padding = [10, 10, 10, 10]
        b.size_hint = (0.5, 1)
        b.pos_hint = {'x': 0.25}
        b.pos = (0, 0)
        b.spacing = 20

        title = standardTitle('Connexion')
        b.add_widget(title)

        self.nom = standardTextField('Identifiant')
        self.mdp = standardTextField('Mot de passe')
        self.mdp.password = True
        b.add_widget(self.nom)
        b.add_widget(self.mdp)

        btn = Button(text='Valider')
        btn.size_hint = (1, .4)
        btn.on_press = self.validating

        bouttonRetour = Button(text='Retour')
        bouttonRetour.on_press = self.retour

        self.connexionRefused = Label()
        self.connexionRefused.text  = "Mot de passe incorrect"
        self.connexionRefused.opacity = 0

        b.add_widget(btn)
        b.add_widget(bouttonRetour)
        b.add_widget(self.connexionRefused)
        self.add_widget(b)

    def retour(self):
        sm.current = 'pickLogin'

    def validating(self):
        infos = self.getFields()
        pseudo, mdp = infos

        user = login_user(pseudo, mdp)
        if user == None:
            self.connexionRefused.opacity = 1
        else:
            sm.current = 'home'

        self.clearFields()

    def getFields(self):
        nom = self.nom.text
        mdp = self.mdp.text
        return (nom, mdp)

    def clearFields(self):
        self.nom.text = ''
        self.mdp.text = ''
