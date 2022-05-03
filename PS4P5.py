lname = str(input("what is your last name"))
pay = int(input("enter salary"))
jobl = int(input("enter job level"))

if jobl > 10:
  bonus = 0.25
if jobl < 9 > 5:
  bonus = 0.20
if jobl < 5:
  bonus = 0.10
bon = bonus * pay
tpay = pay + bon
print(lname," your total pay is $", tpay)
  