class employee:
  def init(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
  def bonus(self, bonuspay):
    b = float(bonuspay)* float(self.pay)
    return b 

class manage(employee):
  def mbonus(self,mngrbonus):
    b = float(mngrbonus) * float(self.pay)
    return b

empl1 = employee('sean', 'patel', 10000)
mana1 = manage('rishi', 'patel', 10000)
bonusrate = input("enter bonus rate")
mgrbonus = 0.40
print(empl1.first)
print(empl1.last)
print(empl1.bonus(bonusrate))
print(empl1.mbonus(mgrbonus))

  
