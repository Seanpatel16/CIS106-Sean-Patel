start = str(input("do you want to run program "))
def fore(month,sales):
  if month == "jan" or "feb" or "mar":
    per = 0.10
  if month == "apr" or "may" or "jun":
    per = 0.15
  if month == "jul" or "aug" or "sept":
    per = 0.20
  if month == "oct" or "nov" or "dec":
    per = 0.25
  tsales = sales * (1+per)
  return tsales

  

while start == "yes":
  lname = str(input("enter last name "))
  month = str(input("enter the month "))
  sales = int(input("enter sales $"))
  tsales = fore(month,sales)
  print("the projected sales are $",tsales)
