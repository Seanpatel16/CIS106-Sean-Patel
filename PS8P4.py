start = str(input("would you like to run this program "))
def mile(miles):
  if miles > 30:
    price = 12
  if miles < 29 > 20:
    price = 10
  if miles < 19 > 10:
    price = 8
  if miles < 10:
    price = 5
  return price
  

while start == "yes":
  lname = str(input("enter your last name "))
  miles = int(input("enter distance from chicago "))
  price = mile(miles)
  sprice = price + price
  print("the cost will be $",price)
  print("the total cost will be $",sprice)
  
