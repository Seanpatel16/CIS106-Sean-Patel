lname = str(input("enter your last name"))
app = int(input("enter price of applaniance"))
if app > 1000:
  per = 0.10
if app < 1000:
  per = 0.05
warren = per * app
tcost = warren + app
print(lname, "the warrenty cost", warren, "the total cost is",tcost )
