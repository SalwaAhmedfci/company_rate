import sqlalchemy
from sqlalchemy.orm import sessionmaker
from database_setup import *
import sqlalchemy
from sqlalchemy.orm import sessionmaker
# opening connection with database
engine = sqlalchemy.create_engine('sqlite://///home/salwa/PycharmProjects/company_rate/data.sqlite')
Base.metadata.bind = engine
# Clear database

Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()




