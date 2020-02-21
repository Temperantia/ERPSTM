from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from frontend.widgets.title import standardTitle
from frontend.widgets.text_field import standardTextField
from kivy.uix.button import Button
from kivy.uix.label import Label
from frontend.globals import sm
from backend.register import order

class Order(Screen):
    amount = None
    description = None
    def __init__(self, **kwargs):
        super(Order, self).__init__(**kwargs)
        b = BoxLayout(orientation='vertical')
        b.padding = [10, 10, 10, 10]
        b.size_hint = (0.5, 1)
        b.pos_hint = {'x': 0.25}
        b.pos = (0, 0)
        b.spacing = 20

        title = standardTitle('Enregistrement d\'une commande')
        self.amount = standardTextField("Montant de la commande")
        self.amount.input_filter = 'float'
        self.description = standardTextField("Description de la commande")

        validatingButton = Button(text = "Valider")
        validatingButton.on_press = self.validate

        goBackButton = Button(text = "Retour")
        goBackButton.on_press = self.goBack

        b.add_widget(title)
        b.add_widget(self.amount)
        b.add_widget(self.description)
        b.add_widget(validatingButton)
        b.add_widget(goBackButton)

        self.add_widget(b)

    def goBack(self):
        sm.current = 'home'

    def validate(self):
        self.getFields()
        self.clearFields()
        self.goBack()

    def getFields(self):
        amount = self.amount.text
        description = self.description.text
        order(amount,description)

    def clearFields(self):
        self.amount.text = ''
        self.description.text = ''
