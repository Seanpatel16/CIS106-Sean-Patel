def mpg(gal,miles):
  mpg1 = float(miles)/float(gal)
  return mpg1
def cost(gal):
  tcost = gal * 2.50
  return tcost
city = input("enter city ")
gal= float(input("enter amount of gallons used "))
miles = float(input("enter amount of miles driven   "))
tcost = cost(gal)
mpg1= mpg(gal, miles)
print(city,"your mpg will be", mpg1, "it will cost $", tcost)