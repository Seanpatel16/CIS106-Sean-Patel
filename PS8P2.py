start = str(input("would you like to run the program "))
def sqft(len,wid,hei):
  floor = 2 * (len * wid)
  wall1 = 2 * (len * hei)
  wall2 = 2* (wid * hei)
  total = floor + wall1 + wall2
  gal = total/50
  return gal
while start == "yes":
  len = int(input("Enter the length "))
  wid = int(input("Enter the width "))
  hei = int(input("Enter the height"))
  gal = sqft(len,wid,hei)
  print("the amount of gallons needed is ",gal)