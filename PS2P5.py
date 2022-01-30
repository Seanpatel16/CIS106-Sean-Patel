oprice = input("enter orginal price of the item")
dis = input("enter the discount amount")
percent = float(dis)/100 
damount = float(percent) * float(oprice)
tprice = float(oprice) - float(damount)
print("the total price was")
print(tprice)
print("the discount amount was")
print(damount)