import sqlalchemy
from sqlalchemy.orm import sessionmaker
import config

engine = sqlalchemy.create_engine(
    'mysql+pymysql://root:' + config.MYSQL_ROOT_PASSWORD + '@localhost:3306/erpstm')
Session = sessionmaker(bind=engine)
session = Session()
