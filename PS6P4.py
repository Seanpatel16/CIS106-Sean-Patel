f = open("text", "r")
itemname = f.readline()
c = 0
while itemname !="":
  price = f.readline()
  qua = f.readline()
  eprice = float(qua) * float(price)
  print("Item: ", itemname)
  print("price: $", format(float(price), '10,.2f'))
  print("extended price: $",   format(eprice,'10,.2f'))
  print("quantity: ", format(float(qua),'10,.2f'))
  c = c + 1
  aprice = (eprice + eprice)/c
  itemname = f.readline()
print("the average price is: $ ", format(float(aprice),'10,.2f'))
  

