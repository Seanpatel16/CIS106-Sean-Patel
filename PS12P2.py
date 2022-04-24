import re
def org():
  txt = input("Enter a line of text: ")
  return txt


def rDuplicate(txt):
  txt2 = txt.strip()
  txt3 = re.sub(' +', ' ',txt2)
  txt4 = txt3 [::-1]
  return txt4


def printText(txt):
  print(txt)

orgText = org()
print("The original text is: ")
printText(orgText)

print("\nThe text after ")
UpdatedText = rDuplicate(orgText)
printText(UpdatedText)