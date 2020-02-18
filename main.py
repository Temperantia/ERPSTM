import sqlalchemy as db
from models import User, Fournisseur
from sqlalchemy.orm import sessionmaker

engine = db.create_engine('mysql+pymysql://root:rootroot@localhost:3306/mydb')
Session = sessionmaker(bind=engine)
session = Session()

fournisseur = Fournisseur(idfournisseur=3)
user = User(nom='lol', prenom='ok', interne=True, fournisseur_idfournisseur1=fournisseur.idfournisseur)
session.add_all([fournisseur, user])
session.commit()

#query = db.select([user])
#result = connection.execute(query)
#result = result.fetchall()
#print(result)