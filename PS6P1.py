x = 0
interest = 0
prince = int(input("enter a principle amount = "))
inte = float(input("enter annual interest percent = "))
pri = prince
print(" year ", " begining balance ", " ending balance ")
while x < 5:
  x = x + 1
  prinint = prince
  interest = prince * inte
  prince = prince + interest
  print (format(x) , format(prinint,'.2f'),           format(prince, '.2f'),)
intamount = prince - pri
print("the total intrest rate is $", intamount)