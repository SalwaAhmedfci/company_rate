import sqlalchemy
from sqlalchemy.orm import sessionmaker
from database_setup import *
import pandas as pd
import sqlite3

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
conn = sqlite3.connect('CompainesData.db')
c = conn.cursor()


# Insert a row of data
i = 1
while i < 2001:
    c.execute("INSERT INTO forbesglobal2000_2016(name,profits,marketValue,revenue,industry)VALUES(?,?,?,?,?)",(str(df.name[i]),str(df.profits[i]),str(df.marketValue[i]),str(df.revenue[i]),str(df.industry[i])))
    i = i + 1

i = 1
while i < 731:
    c.execute("INSERT INTO look_up(SIC,industry)VALUES(?,?)", (int(df1.SICCode[i]), str(df1.Description[i])))
    i = i + 1
# Save (commit) the changes
conn.commit()
conn.close()

#printing test
com = session.query(Company).all()
for f in com:
     print(f.name)
     print(f.industry)
     print(f.profits)
     print(f.revenue)
     print(f.marketValue)



