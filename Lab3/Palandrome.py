testWord = raw_input("enter a word to check:")
testWord.replace(" ","")
length = len(testWord)
halfLength = int(length/2)

for i in range(0, halfLength):
  if testWord[i] != testWord[(length - 1) - i]:
    print "not a palandrome"
    break
  if i == (halfLength -1):
     print "is a palandrome"
