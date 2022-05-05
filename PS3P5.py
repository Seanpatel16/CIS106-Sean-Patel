lname = str(input("enter last name"))
depend = int(input("enter number of dependents"))
gross = int(input("enter your gross income"))
deduct = depend *12000
tgross = deduct - gross
if tgross > 50000:
  tax = 0.20
if tgross < 50000:
  tax = 0.10
taxa = tgross - tax
if taxa <= 0:
  tax = 0
print(lname, "your gross income is ", gross, "the number of dependents is", depend, "your adjusted gross experience", tgross, "your total tax is", tax)