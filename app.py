from kivy.app import App

from frontend.screens.register import Register
from frontend.screens.login import Login
from frontend.screens.landing import PickRegisterOrLogin
from frontend.screens.company import CompanyInformations
from frontend.screens.home import Home

from frontend.screens.order import Order
from frontend.screens.supplierlist import SupplierList
from frontend.sm import sm
from frontend.sc import requestsScreen, suppliersScreen



class MyApp(App):
    def build(self):
        pickLogin = PickRegisterOrLogin(name='pickLogin')
        login = Login(name='login')
        register = Register(name='register')
        companyInformations = CompanyInformations(name='companyInformations')
        home = Home(name='home')
        order = Order(name ='order')
        supplierList = SupplierList(name = 'supplierList')
        sm.add_widget(pickLogin)
        sm.add_widget(login)
        sm.add_widget(register)
        sm.add_widget(companyInformations)
        sm.add_widget(home)
        sm.add_widget(requestsScreen)
        sm.add_widget(suppliersScreen)
        sm.add_widget(order)
        sm.add_widget(supplierList)

        return sm


MyApp().run()
