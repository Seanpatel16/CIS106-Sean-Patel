def batave(hits,bats):
  total = float(hits)/float(bats)
  return total
lname = input("enter your last name ")
bats = float(input("Enter amount of bats "))
hits = float(input("Enter amount of hits "))
total = batave(hits, bats)
print(lname, "your batting average is", total)
