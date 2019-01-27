import sqlalchemy
from sqlalchemy.orm import sessionmaker
from database_setup import *
import pandas as pd
# opening connection with database

engine = create_engine('sqlite:///CompainesData.db')
Base.metadata.bind = engine
# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

df = pd.read_csv("forbesglobal2000-2016.csv")
df1 = pd.read_csv("SIC.csv")
#uri`, `rank`, `name`, `country`, `profits`, `marketValue`, `ceo`, `revenue`, `headquarters`, `industry`, `state`, `SIC`
# market valuation, revenue, profits and industry
profit_column = df.profits
name_column = df.name
industry_column = df.industry
revenue_column = df.revenue
marketvalue_column = df.marketValue
industry_column_f = df1.Description
SIC_column = df1.SICCode
#print (SIC_column)
# for i in revenue_column:
#     print(i)


company = []
i = 1
while i < name_column.__len__():
    company[i] = Company(name = name_column[i] , industry=industry_column[i], marketValue = marketvalue_column[i] , profits = profit_column[i] ,
                         revenue = revenue_column[i] )

    i = i +1
for i in company:
    session.add(i)
    session.commit()


# printing test
com = session.query(Company).all()
for f in com:
    print(f.name)
    print(f.industry)
    print(f.profits)
    print(f.revenue)
    print(f.marketValue)



