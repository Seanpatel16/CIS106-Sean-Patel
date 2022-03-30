def ave(lname,exam1,exam2,exam3):
  testave = (exam1 + exam2 + exam3)/3
  tpoint = exam1 + exam2 + exam3
  return testave, tpoint

lname = str(input("enter last name "))
exam1 = float(input("enter test score 1 "))
exam2 = float(input("enter test score 2 "))
exam3 = float(input("enter test score 3 "))

testave,tpoint = ave(lname,exam1,exam2,exam3)
print(lname, "your average was ",testave, "your total points was ",tpoint)