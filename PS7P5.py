def tuition(hours,dis):
  if dis == "I":
    cost = 250
  if dis == "O":
    cost = 550
  tcost  = float(cost) * float(hours)
  return tcost
lname = input("Enter last name")
dis = input("enter district code")
hours = float(input("Enter credit hours"))
tcost = tuition(hours, dis)
print(lname, "your total cost is $",tcost)