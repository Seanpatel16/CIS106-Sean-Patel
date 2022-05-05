qua = input("enter the quantity of the item")
if qua > 1000:
  price = 3
else:
  price = 5
tprice = price * qua
extprice = (tprice * 0.07) + tprice
print("the quantity was",qua," the unit price was $", price,"the extended price was ",extprice  )

  


