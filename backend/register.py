from models import User, Supplier, Role
from session import session

def supplier(comp_name, addr, status, turnov, headcnt, author):
    supp = Supplier(name = comp_name, address = addr , legal_status = status, turnover = turnov, headcounts = headcnt, authorized = author)
    session.add(supp)
    session.commit()


def register_user(firstnm, lastnm, pseudo, passwd, is_supplier, id_sup, id_rol):
    user = User(firstname = firstnm, lastname = lastnm, personal_id = pseudo, password = passwd, internal = is_supplier, id_supplier = id_sup, id_role = id_rol)
    session.add(user)
    session.commit()

def role(nme):
    rol = Role(name = nme)
    session.add(rol)
    session.commit()

role("Chef")
supplier("Google", "8 rue des pack", "SARL", 10000, 30, True)
register_user("Eric", "SOM DUTT", "Bibirani", "ERIc5372", True, 2, 4) 
