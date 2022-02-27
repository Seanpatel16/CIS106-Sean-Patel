f = open("text", "r")
lastname = f.readline()
bonus = 0
c = 0
Br = 0

while lastname != "":
  salary = f.readline()
  if float(salary) >= float(100000):
    Br = 0.20
  if float(salary) == 50000:
    Br = 0.15
  if float(salary) < 50000:
    Br = 0.10
  bonus = float(salary) * float(Br)
  lastname = f.readline()
  c = c + 1
  totalbonus = (bonus + bonus + bonus)

  print("Employe Last Name: ", lastname)
  print("Employee Salary: $", format(float(salary), '10,.2f'))
  print("Employee Bonus: $", format(bonus,'10,.2f'))

print(totalbonus)
f.close()

  



    


  
    
   
  



