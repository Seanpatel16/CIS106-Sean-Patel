def payrate(jcode):
  if jcode == "L":
    pay = 25
  if jcode == "A":
    pay = 30
  if jcode == "J":
    pay = 50
  return pay
def gpay(pay, hours):
  gross = float(pay) * float(hours)
  return gross

jcode = input("Enter job code")
hours = float(input("enter hours worked"))
pay = payrate(jcode)
gross = gpay(pay, hours)
print("your job code is", jcode, "your pay rate is", pay, "your gross pay is $",gross)
