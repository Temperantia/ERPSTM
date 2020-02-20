from models import User, Supplier, Role
from session import session

def supplier():
    supp = Supplier(name = 'Google', address = '3 rue des Pacquerettes', legal_status = 'GOOD', turnover = 100000, headcounts = 20, authorized = True, status = 'GOOD')
    session.add(supp)
    session.commit()

def register():
    user = User(firstname='ed', lastname='Ed Jones', internal = True, id_supplier = '1', id_role = '2', password = 3246342)
    session.add(user)
    session.commit()

def role():
    rol = Role(name = 'Chef')
    session.add(rol)
    session.commit()

role()
supplier()
register()
