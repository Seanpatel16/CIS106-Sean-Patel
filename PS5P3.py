code = str(input("enter yes or no "))
scount = 0
if code == "yes":
    while code == "yes":
        lname = str(input("enter your last name "))
        score1 = int(input("enter the first test score "))
        score2 = int(input("enter second test score "))
        scount = scount + 1
        ave = (score1 + score2) / 2
        print(lname, "your average was %", ave)
        print("student count = ", scount)
else:
    print("bye")
