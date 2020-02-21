from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from frontend.widgets.title import standardTitle
from backend.requests import get_requests
from frontend.globals import sm
from kivy.uix.label import Label

class Requests(Screen):
    def __init__(self, **kwargs):
        super(Requests, self).__init__(**kwargs)
        requests = get_requests()
        b = BoxLayout(orientation='vertical')
        b.padding = [10, 10, 10, 10]
        b.pos = (0, 0)
        b.spacing = 40
        layout = GridLayout(cols=6)
        layout.add_widget(Label(text='Date'))
        layout.add_widget(Label(text='Statut'))
        layout.add_widget(Label(text='Nature'))
        layout.add_widget(Label(text='Montant'))
        layout.add_widget(Label(text='Payée'))
        layout.add_widget(Label(text='Commentaire'))
        for request in requests:
            layout.add_widget(Label(text=str(request.timestamp)))
            layout.add_widget(Label(text=request.supp_status))
            layout.add_widget(Label(text=request.order_nature))
            layout.add_widget(Label(text=str(request.order_amount)))
            layout.add_widget(Label(text=str(request.order_ispaid)))
            layout.add_widget(Label(text=str(request.opinion)))
        b.add_widget(layout)

        buttnLogin = Button()
        buttnLogin.text = 'Retour'
        buttnLogin.on_press = self.goBack
        b.add_widget(buttnLogin)
        self.add_widget(b)

    def goBack(self):
        sm.current = 'home'