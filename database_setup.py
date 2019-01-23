import os
import sys
from cgitb import text
from flask import Flask
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask import jsonify
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy


# from flask_bootsrap import Bootstrap

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite://///home/salwa/PycharmProjects/company_rate/data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#`uri`, `rank`, `name`, `country`, `profits`, `marketValue`, `ceo`, `revenue`, `headquarters`, `industry`, `state`, `SIC`



class fobres(db.Model):
    __tablename__ = 'forbesglobal2000_2016'

    id = db.Column('id',db.Integer, primary_key=True)
    name = db.Column('name',db.String(250))
    uri = db.Column('uri',db.String(250))
    rank = db.Column('rank',db.String(250))
    country = db.Column('country',db.String(250))
    profits= db.Column('profits',db.String(250))
    marketValue = db.Column('marketValue',db.String(250))
    ceo = db.Column('ceo',db.String(250))
    revenue = db.Column('revenue',db.String(250))
    headquarters = db.Column('headquarters',db.String(250))
    industry = db.Column('industry',db.String(250))
    state = db.Column('state',db.String(250))
    SIC = db.Column('SIC',db.String(250))




