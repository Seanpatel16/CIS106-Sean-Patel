class car:
  def init(self,make,model,stickerprice,discount):
    self.make = make
    self.model = model
    self.stickerprice = stickerprice
    self.discount = discount

    def SW(self,sportwheel):
      b = float(sportwheel) * float(self.stickerprice)
      return b 
    def SE(self, sportengine):
      b = float(sportengine) * float(self.stickerprice)
      return b 
    def SI(self, sportint):
      b = float(sportint) * float(self.stickerprice)
      return b 
class Sport(car):
  def options(self, option):
    b = float(option) * float(self.stickerprice)
    return b 
  

car1 = car('Ferrari', '458', 2000000)
sport1 = Sport('Ferrari', ' 488 Pista', 3500000 )
upgrades = input("enter options on car")
sportwheel = 1000.00
sportengine = 3000.00
sportint = 2000.00
print(car1.make)
print(car1.model)
print(car1.stickerprice)
print(sport1.upgrades(options))
    
    

