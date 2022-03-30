def bowl(score1,score2,score3):
  ave = (score1+score2+score3)/3
  handi = (ave - 220)*0.90
  return handi,ave

lname = str(input("Enter last name"))
score1 = float(input("enter score 1"))
score2 = float(input("enter score 2"))
score3 = float(input("enter score 3"))
handi,ave =bowl(score1,score2,score3)
print(lname, " your average was",ave,"your handicap is ",handi)