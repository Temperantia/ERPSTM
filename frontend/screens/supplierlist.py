from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from frontend.widgets.title import standardTitle
from frontend.widgets.text_field import standardTextField
from kivy.uix.button import Button
from kivy.uix.label import Label
from frontend.globals import sm, user

class SupplierList(Screen):
    nom = None
    mdp = None
    connexionRefused = None

    def __init__(self, **kwargs):
        super(SupplierList, self).__init__(**kwargs)
        b = BoxLayout(orientation='vertical')
        b.padding = [10, 10, 10, 10]
        b.size_hint = (0.5, 1)
        b.pos_hint = {'x': 0.25}
        b.pos = (0, 0)
        b.spacing = 20

        title = standardTitle('Liste des fournisseurs')
        b.add_widget(title)
        self.add_widget(b)

