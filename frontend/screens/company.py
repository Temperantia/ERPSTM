from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from frontend.widgets.title import standardTitle
from frontend.widgets.text_field import standardTextField
from frontend.globals import sm
from backend.register import supplier


class CompanyInformations(Screen):
    effectif = None
    turnOver = None
    companyName = None
    mainbutton = None
    SIREN = None
    contact = None

    def switchStatutJuridique(self, numero):
        nom = ''
        if (numero == 0):
            nom = 'SARL'
        elif (numero == 1):
            nom = 'SA'
        elif (numero == 2):
            nom = 'SAS'
        elif (numero == 3):
            nom = 'EURL'
        elif (numero == 4):
            nom = 'EI'
        return nom

    def __init__(self, **kwargs):
        super(CompanyInformations, self).__init__(**kwargs)
        b = BoxLayout(orientation='vertical')
        b.padding = [10, 10, 10, 10]
        b.pos = (0, 0)
        b.spacing = 20
        b.size_hint = (0.5, 1)
        b.pos_hint = {'x': 0.25}

        title = standardTitle(
            'Renseignement des informations de l\'entreprise')

        dropdown = DropDown()
        for index in range(5):

            nom = self.switchStatutJuridique(index)

            btn = Button(text=nom, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)

        self.mainbutton = Button(text='Statut Juridique', size_hint=(1, .5))
        self.mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance,
                      x: setattr(self.mainbutton, 'text', x))

        self.turnOver = standardTextField('Chiffre d\'affaires en €')
        self.turnOver.input_filter = 'float'
        self.effectif = standardTextField('Nombres d\'employés')
        self.effectif.input_filter = 'float'
        self.companyName = standardTextField('Nom de l\'entreprise')
        self.SIREN = standardTextField('Numéro SIREN')
        self.contact = standardTextField('Coordonnés')

        validatingButton = Button()
        validatingButton.text = 'Valider'
        validatingButton.on_press = self.validating

        backButton = Button()
        backButton.text = 'Retour'
        backButton.on_press = self.goBack

        b.add_widget(title)
        b.add_widget(self.mainbutton)
        b.add_widget(self.companyName)
        b.add_widget(self.turnOver)
        b.add_widget(self.effectif)
        b.add_widget(self.SIREN)
        b.add_widget(self.contact)
        b.add_widget(validatingButton)
        b.add_widget(backButton)

        self.add_widget(b)

    def goBack(self):
        sm.current = "home"        

    def validating(self):
        self.getFields()
        self.clearFields()
        self.goBack()

    def getFields(self):
        legalStatus = self.mainbutton.text
        effectif = self.effectif.text
        turnOver = self.turnOver.text
        companyName = self.companyName.text
        SIREN = self.SIREN.text
        contact = self.contact.text
        supplier(legalStatus,companyName,turnOver,effectif,SIREN,contact)

    def clearFields(self):
        self.effectif.text = ''
        self.turnOver.text = ''
        self.companyName.text = ''
        self.SIREN.text = ''
        self.contact.text = ''
