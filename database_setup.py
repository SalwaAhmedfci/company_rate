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


class look_up(Base):
    __tablename__ = "look_up"

#contains mapping between SIC and indusrty
    id = Column(Integer, primary_key=True)
    SIC = Column(Integer, nullable=False)
    industry = Column(String(250), nullable=False)


class Company(Base):
    __tablename__ = 'forbesglobal2000_2016'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    profits = Column(String(250), nullable=False)
    marketValue = Column(String(250), nullable=False)
    revenue = Column(String(250), nullable=False)
    industry = Column(String(250), ForeignKey('look_up.industry'))
    Indusrty = relationship(look_up)


class SIC(Base):
    __tablename__ = "SIC"

    # contains mapping between SIC and keywords
    id = Column(Integer, primary_key=True)
    SIC = Column(Integer, ForeignKey('look_up.SIC'))
    keywords = Column(String(250), nullable=False)


# configuration part
engine = create_engine('sqlite:///CompainesData.db')

Base.metadata.create_all(engine)