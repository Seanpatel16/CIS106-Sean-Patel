def sales(sale):
  if sale < 50000:
    com = 0.05
  if sale > 100000:
    com = 0.10
  coma = com * sale
  sal = sale * 0.05
  salet = sale + sal
    
  return coma, salet

lname = str(input("enter last name "))
sale = float(input("enter sales amount $"))
coma,salet = sales(sale)
print(lname, "the total commission was $", coma , "the target for next year is $", salet )