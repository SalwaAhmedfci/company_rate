from database_setup import *



fobres = fobres.query.all()

for f in fobres:
   print(f.id)
   print(f.industry)
   print(f.profits)
   print(f.revenue)
   print(f.market_value)

