qua = int(input("enter quantity of books"))
cost = int(input("enter the price of books"))
if cost > 50:
  ship = 0
if cost < 50:
  ship = 25
tprice = cost*qua+ship
print("the total cost is ",tprice, "the shipping cost was", ship)

  