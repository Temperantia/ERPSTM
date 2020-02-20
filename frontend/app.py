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
from kivy.uix.dropdown import DropDown #pour utilisation de menu deroulants
from kivy.base import runTouchApp


def standardTextField(text):
    t = TextInput()
    t.hint_text = text
    t.font_size = 22
    t.focus = True
    t.size_hint_max_y = 40
    t.multiline = False
    return t

"""
Creer un titre standard contenant le texte fourni en argument
"""
def standardTitle(text):
        title = Label()
        title.text = text
        title.bold = True
        title.font_size = 26
        return title


class Login(Screen):
    nom = None
    mdp = None

    def __init__(self, **kwargs):
        super(Login, self).__init__(**kwargs)
        b = BoxLayout(orientation='vertical')
        b.padding = [10, 10, 10, 10]
        b.size_hint = (0.5,1)
        b.pos_hint = {'x' : 0.25} 
        b.pos = (0, 0)
        b.spacing = 40

        title = standardTitle("Connexion")
        b.add_widget(title)

        self.nom = standardTextField("Pseudo")
        self.mdp = standardTextField("Mot de passe")
        self.mdp.password = True
        b.add_widget(self.nom)
        b.add_widget(self.mdp)

        btn = Button(text="Valider")
        btn.size_hint = (1,.4)
        btn.on_press = self.validating

        bouttonRetour = Button(text = "Retour")
        bouttonRetour.on_press = self.retour
        
        l = Label(text="")

        b.add_widget(btn)
        b.add_widget(bouttonRetour)
        b.add_widget(l)
        self.add_widget(b)

    def retour(self):
        MyApp.sm.current = 'pickLogin'


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


class Register(Screen):
    firstName = None
    lastName = None
    pseudo = None
    passwd = None
    buttnSupplierIntern = Button()
    supplier = True         #true if is a supplier, false if is an intern
    def __init__(self, **kwargs):
        super(Register, self).__init__(**kwargs)
        b = BoxLayout(orientation='vertical')
        b.padding = [10, 10, 10, 10]
        b.pos = (0, 0)
        b.spacing = 20
        b.size_hint = (0.5,1)
        b.pos_hint = {'x' : 0.25} 

        title = standardTitle("Inscription")
        b.add_widget(title)

        #TO DO ajout du poste
        self.firstName = standardTextField("Prénom")
        self.lastName = standardTextField("Nom")
        self.pseudo = standardTextField("Pseudo")
        self.passwd = standardTextField("Mot de passe")

        self.passwd.password = True

        b.add_widget(self.firstName)
        b.add_widget(self.lastName)
        b.add_widget(self.pseudo)
        b.add_widget(self.passwd)

        self.buttnSupplierIntern.text = "Cliquez pour choisir votre statut"
        self.buttnSupplierIntern.on_press = self.changeStatus
        
        b.add_widget(self.buttnSupplierIntern)

        btn = Button(text="Valider")
        btn.on_press = self.validating

        bouttonRetour = Button(text = "Retour")
        bouttonRetour.on_press = self.retour

        b.add_widget(btn)
        b.add_widget(bouttonRetour)
        self.add_widget(b)

    def retour(self):
        MyApp.sm.current = 'pickLogin'

    def changeStatus(self):
        if(self.supplier):
            message = "Vous êtes un Interne" +'\n' + "Cliquez pour changer"
            self.buttnSupplierIntern.text = message
            self.supplier = False

        else:
            message = "Vous êtes un Fournisseur" +'\n' + "Cliquez pour changer"
            self.buttnSupplierIntern.text = message
            self.supplier = True

    def validating(self):
        info = self.getFields()
        self.clearFields()
        

    def getFields(self):
        firstName = self.firstName.text
        lastName = self.lastName.text
        pseudo = self.pseudo.text
        passwd = self.passwd.text

        #a delete une fois le lien avec le back effectué
        print("prenom " + firstName)          
        print("nom " + lastName)                
        print("pseudo " + pseudo)          
        print("mot de passe " + passwd)        
        return (firstName, lastName, pseudo, passwd)

    def clearFields(self):
        self.firstName.text = ""
        self.lastName.text = ""
        self.pseudo.text = ""
        self.passwd.text = ""
        
class PickRegisterOrLogin(Screen):
    def __init__(self, **kwargs):
        super(PickRegisterOrLogin, self).__init__(**kwargs)
        b = BoxLayout(orientation='vertical')
        b.padding = [10, 10, 10, 10]
        b.pos = (0, 0)
        b.spacing = 40
        b.size_hint = (0.5,1)
        b.pos_hint = {'x' : 0.25}

        title = standardTitle("Identifiez-vous")
        b.add_widget(title)

        buttnLogin = Button()
        buttnLogin.text = "J'ai déjà un compte"
        buttnLogin.on_press = self.goToLoginScreen

        buttnRegister = Button()
        buttnRegister.text = "Je n'ai pas de compte"
        buttnRegister.on_press = self.goToRegisterSreen

        b.add_widget(buttnLogin)
        b.add_widget(buttnRegister)

        l = Label()
        b.add_widget(l)
        self.add_widget(b)

    def goToLoginScreen(self):
        MyApp.sm.current = 'login'

    def goToRegisterSreen(self):
        MyApp.sm.current = 'register'

class CompanyInformations(Screen):
    def switchStatutJuridique(self,numero):
        nom = ""
        if (numero == 0):
            nom = "SARL"
        if (numero == 1):
            nom = "SA"
        if (numero == 2):
            nom = "SAS"
        if (numero == 3):
            nom = "EURL"
        if (numero == 4):
            nom = "EI" 
        return nom

    def __init__(self, **kwargs):
        super(CompanyInformations, self).__init__(**kwargs)
        b = BoxLayout(orientation='vertical')
        b.padding = [10, 10, 10, 10]
        b.pos = (0, 0)
        b.spacing = 40
        b.size_hint = (0.5,1)
        b.pos_hint = {'x' : 0.25}

        title = standardTitle("Renseignements des informations d'entreprises")

        dropdown = DropDown()
        for index in range(5):

            nom = self.switchStatutJuridique(index)

            btn = Button(text = nom, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        mainbutton = Button(text='Statut Juridique', size_hint=(1, .5))
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))


        turnOver = standardTextField("Chiffre d'affaires en €")
        turnOver.input_filter = 'float'

        effectif = standardTextField("Nombres d'employés")
        
        validatingButton = Button()
        validatingButton.text = "Valider"

        b.add_widget(title)
        b.add_widget(mainbutton)
        b.add_widget(turnOver)
        b.add_widget(effectif)
        b.add_widget(validatingButton)

        self.add_widget(b)

class MyApp(App):

    sm = ScreenManager()
    def build(self):
        
        pickLogin = PickRegisterOrLogin(name = 'pickLogin')
        login = Login(name='login')
        register = Register(name = 'register')
        companyInformations = CompanyInformations(name = 'companyInformations')
        
        self.sm.add_widget(pickLogin)
        self.sm.add_widget(login)
        self.sm.add_widget(register)
        self.sm.add_widget(companyInformations)
        self.sm.current = 'companyInformations'
        
        #ligne inutile

        return self.sm


MyApp().run()
