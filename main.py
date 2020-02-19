from models import User, Supplier
from session import session

supplier = Supplier()
session.add(supplier)
session.commit()
print(supplier.id)

result = session.query(Supplier).all()
print(result)
