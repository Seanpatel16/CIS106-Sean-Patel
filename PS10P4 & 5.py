
f = open("txt","r")

def search(lastn,sname):
  l = len(lastn)
  sindex = -1
  for y in range(0,l,1):
    if lastn[y] == sname:
      sindex = y
      
  return(sindex)

lastn=[]
bat=[]
lastn = f.readline()

response = input("do you want to run this program yes or no")
while response == "yes":
  sname = input("enter the last name")
  i = search(lastn,sname)
  if i == 1:
    print(sname,"not in array")
  else:
    print(lastn[i],"batting average ",bat[i])
search(lastn,sname)


f.close()