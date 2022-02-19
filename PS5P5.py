code = str(input("Would you like to run this program yes or no "))
aprice = 0
again = str("yes")
if code == "yes" and again == "yes":
  while code == "yes":
    qua = int(input("enter the number of quanity for the project "))
    price = int(input("enter the price of each item "))
    eprice = qua * price
    if eprice > 100000.00:
      dis = eprice * 0.25
    else:
      dis = eprice * 0.10
    tprice = eprice - dis
    aprice = aprice + tprice
    print("the total price was $", tprice, "the total discount was $",dis, " the total of all orders is $", aprice)
    again = str(input("would you like to use to program again "))
else:
  print("Thank you have a good day")