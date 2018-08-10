import math
for i in range(100,200):
    flag=0
    for j in range(2,round(math.sqrt(i))):
        if i%j==0:
            flag=1
            break
    if flag:
        continue
    print(i)
