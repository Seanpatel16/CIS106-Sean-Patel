class Employee:
  def __init__(self, first, last, pay,bonus):
    self.first = first
    self.last = last
    self.email = first + '.' + last +'@email.com'
    self.bonus = bonus
    self.pay = pay
    bonus = pay * b

  def fullname(self):
    return '{} {}'.format(self.first, self.last)

b = int(input("enter bonus rate "))
emp_1 = Employee('Corey', 'Schafer', 50000,b)
emp_2 = Employee('Sean', 'Patel', 60000,b)

        
emp_1.fullname()
print(Employee.fullname(emp_1), emp_1.pay, "bonus = $",emp_1.bonus)
print(Employee.fullname(emp_2), emp_2.pay, "bonus = $",emp_2.bonus)