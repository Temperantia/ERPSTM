import sqlalchemy
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('mysql+pymysql://root:1174661089@localhost:3306/erpstm')
Session = sessionmaker(bind=engine)
session = Session()