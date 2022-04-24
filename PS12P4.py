def repeatShift(line):
  characters = int(input("Enter no. of characters  to print in each lines: "))
  linenum = int(input("Enter no. of lines to print: "))
  Named = input("Enter scroll direction of Line: Right: r || Left: l -> ")
  shi = ""
  if Named == "r":
    shi = ""
  elif Named == "l":
    shi = " " * (linenum - 1)
    counter = 0
  for i in range(linenum):
    print(shi, end='')
    if Named == "r":
       shi += " "
    elif Named == "l":
      shi = shi[:-1]
    for j in range(characters):                
      print(line[counter], end='')
      counter = (counter + 1) % len(line)
    print()

if __name__ == '__main__':
  line = input("Enter the line of text: ")
  repeatShift(line)
  

