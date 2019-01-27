import os
import sys
from cgitb import text

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask import jsonify

Base = declarative_base()

#`uri`, `rank`, `name`, `country`, `profits`, `marketValue`, `ceo`, `revenue`, `headquarters`, `industry`, `state`, `SIC`



class Company(Base):
    __tablename__ = 'forbesglobal2000_2016'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    #uri = Column(String(250), nullable=False)
    #rank = Column(String(250), nullable=False)
    #county = Column(String(250), nullable=False)
    profits = Column(String(250), nullable=False)
    marketValue = Column(String(250), nullable=False)
    #ceo = Column(String(250), nullable=False)
    revenue = Column(String(250), nullable=False)
   # headquarters = Column(String(250), nullable=False)
    industry = Column(String(250), nullable=False)
    #state = Column(String(250), nullable=False)




class SIC(Base):
    __tablename__ = "SIC"


    id = Column(Integer, primary_key=True)
    SIC = Column(Integer, nullable=False)
    Industry_name = Column(String(250), ForeignKey('forbesglobal2000_2016.industry'))
    Indusrty = relationship(Company)


# configuration part
engine = create_engine('sqlite:///CompainesData.db')

Base.metadata.create_all(engine)