def comp(qua,price):
  total = price*qua 
  tax = total * 0.07
  t = total + price
  return t,tax

qua = float(input("Enter the quantity"))
price = float(input("enter the price"))
t,tax = comp(qua,price)
print("your total is $", t, " your tax total is $", tax)
  