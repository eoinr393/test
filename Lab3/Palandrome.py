testWord = raw_input("enter a word to check:")
testWord.replace(" ","")
length = len(testWord)
halfLength = int(length/2)
#for loop checks the first character against the last,
#then moves in a step and checks the next two sets,
#because half of the length is an int there are no problems with odd numbers
for i in range(0, halfLength):
  if testWord[i] != testWord[(length - 1) - i]:
    print "not a palandrome"
    break
  if i == (halfLength -1):
     print "is a palandrome"
