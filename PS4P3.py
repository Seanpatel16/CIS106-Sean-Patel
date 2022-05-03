princ = int(input("enter the princple amount of CD"))
years = int(input("enter the years of maturity"))
if princ > 100000:
  int = 0.06
if princ > 50000 < 100000:
  int = 0.05
if princ < 50000:
  int = 0.02
total = int * princ 
cdtotal = total + princ
print("the total is ", cdtotal)