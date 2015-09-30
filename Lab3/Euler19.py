#calculate the amount of sundays that fall on the first of each month
#between 1900 and 2000
dayArray = [31, 28, 31,30,31,30,31,31,30,31,30,31]
offset = 0
MonNum = 0

for y in range(0,100):
  for i in range(0,12):
    if y % 4 == 0 and i == 2:
      offset += 1
    else:
      offset += dayArray[i]- 28

    if offset % 7 == 6:
      MonNum += 1

print MonNum
