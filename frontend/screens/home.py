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
        buttnCompanyInfo = Button(text = "Renseigner les informations de l'entreprise")
        buttnCompanyInfo.on_press = self.goToCompany

        buttnOrder = Button(text = "Ajouter une nouvelle commande")
        buttnOrder.on_press = self.goToOrder

        b.add_widget(title)
        b.add_widget(buttnCompanyInfo)
        b.add_widget(buttnOrder)

        buttnLogin = Button()
        buttnLogin.text = 'Liste des fournisseurs'
        buttnLogin.on_press = self.goToSuppliers
        b.add_widget(buttnLogin)

        buttnLogin = Button()
        buttnLogin.text = 'Demandes en cours'
        buttnLogin.on_press = self.goToRequests
        b.add_widget(buttnLogin)
        self.add_widget(b)

    def goToRequests(self):
        sm.current = 'requests'

    def goToSuppliers(self):
        sm.current = 'suppliers'

    def goToOrder(self):
        sm.current = 'order'

    def goToCompany(self):
        sm.current = 'companyInformations'
