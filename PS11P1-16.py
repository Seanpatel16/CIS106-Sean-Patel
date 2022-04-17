#1
L=int(input("Enter number of items: "))
first=[]
for i in range(0,L):
  first.append(int(input()))
print(first)
#2
first.insert(1,99)
print(first)
#3
for i in range(0,len(first)):
  if first[i]==99:
    first[i]=100
print(first)
#4
sec=[500, 600, 700, 800, 900]
print(sec)
#5
sec.remove(800)
print(sec)
#6
first.pop(2)
#7
grades =["A", "B", "B", "C", "D", "C"]
#8
print(grades.count("A"))
#9
print(grades.index("B"))
#10
if "F" not in grades:
  print("F is not in the list")
#11
sec.clear()
print(sec)
#12
#del sec
#print(sec)
#13
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
#14
players.sort()
print(players)
#15
players2=players
print(players2)
#16
players2=sorted(players2, reverse=True)
print(players)
print(players2)