import os
import sys
from cgitb import text

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask import jsonify
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

#`uri`, `rank`, `name`, `country`, `profits`, `marketValue`, `ceo`, `revenue`, `headquarters`, `industry`, `state`, `SIC`

class fobres(Base):
    __tablename__ = 'forbesglobal2000_2016'

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    uri = Column(String(250))
    rank = Column(String(250))
    name = Column(String(250))
    country = Column(String(250))
    profits= Column(String(250))
    marketValue = Column(String(250))
    ceo = Column(String(250))
    revenue = Column(String(250))
    headquarters = Column(String(250))
    industry = Column(String(250))
    state = Column(String(250))
    SIC = Column(String(250))



# configuration part

engine = create_engine('sqlite://///home/salwa/PycharmProjects/company_rate/data.sqlite')

Session = sessionmaker(bind=engine, autocommit=True)
session = Session()
session.begin()
try:
    Fobres = session.query(fobres).all()
    session.commit()

    for f in Fobres:

        print(f.id)
        print(f.industry)
        print(f.profits)
        print(f.revenue)
        print(f.market_value)

except:
    session.rollback()
    raise

#market valuation, revenue, profits and industry
#uri


# for f in forbes:
#    print( f.id)
#    print(f.industry)
#    print(f.profits)
#    print(f.revenue)
#    print(f.market_value)


