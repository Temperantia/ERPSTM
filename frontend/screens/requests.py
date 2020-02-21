from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from frontend.widgets.title import standardTitle
from frontend.widgets.text_field import standardTextField


class Requests(Screen):
    def __init__(self, **kwargs):
        super(Requests, self).__init__(**kwargs)
        requests = [
            {
                'timestamp': 'jlskdf',
                'supp_status': 'sjdlkf',
                'order_nature': 'sjdlkf',
                'order_amount': 23,
            }
        ]
        layout = GridLayout(cols=4)
        for request in requests:
            layout.add_widget(Button(text=request['timestamp']))
            layout.add_widget(Button(text=request['supp_status']))
            layout.add_widget(Button(text=request['order_nature']))
            layout.add_widget(Button(text=str(request['order_amount'])))
        self.add_widget(layout)