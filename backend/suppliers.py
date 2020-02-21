from backend.models import Supplier
from backend.session import session


def get_suppliers():
    suppliers = session.query(Supplier).all()
    return suppliers
