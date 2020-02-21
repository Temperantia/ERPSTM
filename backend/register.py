from backend.models import User, Supplier, Role, Request
from backend.session import session


def supplier(status, comp_name, turnov, headcnt, siren, addss):
    supp = Supplier(legal_status = status, name = comp_name, turnover = turnov, 
                    headcounts = headcnt, num_SIREN = siren, address = addss)
    session.add(supp)
    session.commit()


def register_user(firstnm, lastnm, pseudo, passwd, is_supplier):
    user = User(firstname=firstnm, lastname=lastnm,
                personal_id=pseudo, password=passwd, internal=is_supplier)
    session.add(user)
    session.commit()
    return user


def role(nme):
    rol = Role(name=nme)
    session.add(rol)
    session.commit()

def order(ord_amount, ord_nat):
    ord = Request(order_amount = ord_amount, ord_nature = ord_nat)
    session.add(ord)
    session.commit()

# role('Chef')
#supplier('Google', '8 rue des pack', 'SARL', 10000, 30, True)
#register_user('Eric', 'SOM DUTT', 'Bibirani', 'ERIc5372', True, 2, 4)
