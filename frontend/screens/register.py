from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import Screen

from frontend.widgets.text_field import standardTextField
from frontend.widgets.title import standardTitle
from backend.register import register_user
from frontend.sm import sm
from frontend.globals import user


class Register(Screen):
    firstName = None
    lastName = None
    pseudo = None
    passwd = None
    buttnSupplierIntern = Button()
    supplier = True  # true if is a supplier, false if is an intern

    def __init__(self, **kwargs):
        super(Register, self).__init__(**kwargs)
        b = BoxLayout(orientation='vertical')
        b.padding = [10, 10, 10, 10]
        b.pos = (0, 0)
        b.spacing = 20
        b.size_hint = (0.5, 1)
        b.pos_hint = {'x': 0.25}

        title = standardTitle('Inscription')
        b.add_widget(title)

        # TO DO ajout du poste
        self.firstName = standardTextField('Prénom')
        self.lastName = standardTextField('Nom')
        self.pseudo = standardTextField('Pseudo')
        self.passwd = standardTextField('Mot de passe')

        self.passwd.password = True

        b.add_widget(self.firstName)
        b.add_widget(self.lastName)
        b.add_widget(self.pseudo)
        b.add_widget(self.passwd)

        self.buttnSupplierIntern.text = 'Cliquez pour choisir votre statut'
        self.buttnSupplierIntern.on_press = self.changeStatus

        b.add_widget(self.buttnSupplierIntern)

        btn = Button(text='Valider')
        btn.on_press = self.validating

        bouttonRetour = Button(text='Retour')
        bouttonRetour.on_press = self.retour

        b.add_widget(btn)
        b.add_widget(bouttonRetour)
        self.add_widget(b)

    def retour(self):
        sm.current = 'pickLogin'

    def changeStatus(self):
        if(self.supplier):
            message = 'Vous êtes un Interne' + '\n' + 'Cliquez pour changer'
            self.buttnSupplierIntern.text = message
            self.supplier = False

        else:
            message = 'Vous êtes un Fournisseur' + '\n' + 'Cliquez pour changer'
            self.buttnSupplierIntern.text = message
            self.supplier = True

    def validating(self):
        infos = self.getFields()
        self.clearFields()
        prenom, nom, pseudo, mdp = infos

        user = register_user(prenom, nom, pseudo, mdp, self.supplier)
        sm.current = 'home'

    def getFields(self):
        firstName = self.firstName.text
        lastName = self.lastName.text
        pseudo = self.pseudo.text
        passwd = self.passwd.text

        # a delete une fois le lien avec le back effectué
        return (firstName, lastName, pseudo, passwd)

    def clearFields(self):
        self.firstName.text = ''
        self.lastName.text = ''
        self.pseudo.text = ''
        self.passwd.text = ''
