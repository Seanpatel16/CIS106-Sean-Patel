lastname = ["Scott","Smith","Patel","John","Trivedi","Malik","Ellis","Saint","Thomas","Davidson"]
scores = ["98","84","87","78","98","53","82","65","81","100"]
  
def p(lastname,scores):
  l = len(lastname)
  for y in range(0,l,1):
    print(lastname[y],"exams score was",scores[y])
p(lastname,scores)