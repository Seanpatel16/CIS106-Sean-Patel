tick = int(input("enter number of tickets"))
if tick >= 25:
  price = 50
if tick < 24 < 10:
  price = 60
if tick < 5 > 9:
  price = 70
if tick < 5:
  price = 75
total = price * tick
print("the total price was $", total, "each ticket cost $", price)