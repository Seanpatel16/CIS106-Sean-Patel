code = str(input("enter yes or no if you want to continue this program "))
emp = 0
start = str
tpay = 0
again = str("yes")
if code == "yes":
  while code == "yes" and again == "yes":
    lname = str(input("enter employee last name "))
    hours = int(input("enter the hours worked "))
    pay = int(input("enter the employees payrate "))
    if hours > 40:
      ot = hours - 40
    else:
      hours = hours
      ot = 0
    gpay = (hours * pay)+(ot*(pay*1.5))
    tpay = gpay + tpay
    emp = emp + 1
    print(lname, "your gross pay is $", gpay, "the total employee pay is $", tpay, "number of employees = ", emp)
    again = str(input("would you like to enter another employee yes or no "))
    


else:
 print("bye")

