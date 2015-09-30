firstnum = 1
secondnum = 0
storednum = 0
count = 0

while firstnum/1000 < 1:
  storednum = firstnum
  firstnum = firstnum + secondnum
  secondnum = storednum
  count += 1
print count