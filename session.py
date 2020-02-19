import sqlalchemy
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('mysql+pymysql://root:rootroot@localhost:3306/erpstm')
Session = sessionmaker(bind=engine)
session = Session()