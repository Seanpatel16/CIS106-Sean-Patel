def comptotal(qua, price):
  total = float(qua) * float(price)

  if total > 10000:
    total = total * 0.90
  else:
    total = total
  return total

qua = float(input("enter quantity"))
price = float(input("enter price"))
total = comptotal(qua, price)
print(" The total is $", total)

  