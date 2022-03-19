start = str(input("Would you like to run this program "))
def car(make,model,msrp,code):
  if make == "honda" and model == "accord":
    per = 0.10
  if make == "toyota" and model == "rav4":
    per = 0.15
  if code == "Y":
    per = 0.30
  else:
    per == 0.05
  dis = msrp * per
  tax = msrp * 0.07
  total = msrp + tax - dis
  return total 
  
  
  
    
    


while start == "yes":
  make = str(input("enter the make the of vehicle  "))
  model = str(input("enter the model of the vehicle  "))
  code = str(input("enter electric vehicle code "))
  msrp = int(input("enter MSRP of car $"))
  total = car(make,model,msrp,code)
  print(total)