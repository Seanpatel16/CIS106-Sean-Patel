start = str(input("would you like to run this program "))
def mvalue(county,value):
  if county == "cook":
    avp = 0.90
  if county == "dupage":
    avp = 0.80
  if county == "mchenry":
    avp = 0.75
  if county == "kane":
    avp = 0.60
  else:
    avp = 0.70
  avalue = avp * value
  return avalue

  
while start == "yes":
  county = str(input("enter the county "))
  value = int(input("enter market value of house "))
  avalue = mvalue(county,value)
  print("the value is $",avalue, " and the county was ", county)
  