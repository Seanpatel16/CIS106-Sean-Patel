f = open("text", "r")
lname = f.readline()
pc = 0
c = 0
while lname !="":
  dis = f.readline()
  chours = f.readline()
  if dis != "I":
    pc = 250
  if dis != "O":
    pc = 500
  tprice = float(pc) * float(chours)
  print("Student Last Name:", lname)
  print("the total credit hours:", chours)
  print("the total tuition: $",tprice)
  c = c + 1
  total = tprice + tprice
  lname = f.readline()
print("the total tuiton was: $",total)
print("the total students was:",c )
      



    
