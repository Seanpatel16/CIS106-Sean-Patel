name=input("enter full name ")

l=name.split()
for word in l:
  word=word.strip 
if len(l)==1:
  print("You have entered only firstname or put no space")
else:
  print("{} {}".format(l[1],l[0][0]))