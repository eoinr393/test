originalNum = 100
totNum = 0
sumNum = 0

while originalNum != 1:
  totNum += originalNum * (originalNum - 1)
  originalNum -= 1
print totNum

for i in range(int(totNum/10),0, -1):
  sumNum += int(totNum / (10*i))
print sumNum
