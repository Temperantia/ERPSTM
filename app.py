from kivy.app import App

from frontend.screens.register import Register
from frontend.screens.login import Login
from frontend.screens.landing import PickRegisterOrLogin
from frontend.screens.company import CompanyInformations
from frontend.screens.home import Home
from frontend.screens.requests import Requests
from frontend.screens.order import Order
from frontend.screens.supplierlist import SupplierList
from frontend.globals import sm



class MyApp(App):
    def build(self):
        pickLogin = PickRegisterOrLogin(name='pickLogin')
        login = Login(name='login')
        register = Register(name='register')
        companyInformations = CompanyInformations(name='companyInformations')
        home = Home(name='home')
        requests = Requests(name='requests')
        order = Order(name ='order')
        supplierList = SupplierList(name = 'supplierList')
        sm.add_widget(pickLogin)
        sm.add_widget(login)
        sm.add_widget(register)
        sm.add_widget(companyInformations)
        sm.add_widget(home)
        sm.add_widget(requests)
        sm.add_widget(order)
        sm.add_widget(supplierList)

        sm.current = 'home'

        return sm


MyApp().run()
