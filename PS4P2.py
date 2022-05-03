partn = int(input("enter part number"))
qua = int(input("enter the quantity"))
if partn == 10 or 55:
  price = 1.00
if partn == 99:
  price = 2.00
if partn == 80 or 70:
  price = 3.00
else:
  price = 5.00
total = price * qua 
print(partn, "the price per unit is ", price, "the total price is ",total)

