def dis(qua,price,dr):
  tprice = qua * price
  disa= tprice * (dr/100)
  tdr = tprice - disa
  return disa,tdr
  
qua = float(input("enter quantity of item "))
price = float(input("enter price of the item "))
dr = float(input("enter discount rate of item "))
disa,tdr = dis(qua,price,dr)
print("The discount amount was $", disa)
print("the total price with discount is $", tdr)