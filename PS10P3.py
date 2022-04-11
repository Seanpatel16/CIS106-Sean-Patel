def names(lastn,scores):
  for i in lastn:
    print(i)
  for y in scores:
      print(y)
  l = len(lastn)
  for i in range (0,l,0):
    print(lastn[y],scores[y])
f = open("txt","r")
def hilow(lastn,scores):
  l = len(lastn)
  hiscore = -1.0
  lowscore = 99999
  for y in range (0,l,1):
    if float(scores[y]) > float(hiscore):
      hiindex = y
      hiscore = scores[y]

  if float(scores[y]) < float(lowscore):
    loindex = y
    lowscores = scores[y]

  print("Highest score", lastn[hiindex], scores[hiindex])
  print("Lowest score", lastn[loindex], scores[loindex])
  

      
lastn=[]
scores=[]
lastname = f.readline()
while lastname !="":
  lastn.append(str(lastname).rstrip("/n"))
  s = float(f.readline())
  scores.append(s)
  lastname = f.readline()
f.close()

hilow(lastn,scores)

  
