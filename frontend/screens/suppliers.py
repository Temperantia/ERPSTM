from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from frontend.widgets.title import standardTitle
from frontend.sm import sm
from frontend.globals import suppliers
from kivy.uix.label import Label

class Suppliers(Screen):
    def __init__(self, **kwargs):
        super(Suppliers, self).__init__(**kwargs)
        b = BoxLayout(orientation='vertical')
        b.padding = [10, 10, 10, 10]
        b.pos = (0, 0)
        b.spacing = 40
        layout = GridLayout(cols=7)
        layout.add_widget(Label(text='Nom'))
        layout.add_widget(Label(text='Adresse'))
        layout.add_widget(Label(text='Forme juridique'))
        layout.add_widget(Label(text='Chiffre d\'affaire'))
        layout.add_widget(Label(text='Effectifs'))
        layout.add_widget(Label(text='Autorisée'))
        layout.add_widget(Label(text='SIREN'))
        for supplier in suppliers:
            layout.add_widget(Label(text=str(supplier.name)))
            layout.add_widget(Label(text=str(supplier.address)))
            layout.add_widget(Label(text=str(supplier.legal_status)))
            layout.add_widget(Label(text=str(supplier.turnover)))
            layout.add_widget(Label(text=str(supplier.headcounts)))
            layout.add_widget(Label(text=str(supplier.authorized)))
            layout.add_widget(Label(text=str(supplier.num_SIREN)))
        b.add_widget(layout)

        buttnLogin = Button()
        buttnLogin.text = 'Retour'
        buttnLogin.on_press = self.goBack
        b.add_widget(buttnLogin)
        self.add_widget(b)

    def goBack(self):
        sm.current = 'home'