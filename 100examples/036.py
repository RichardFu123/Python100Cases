lo=int(input('下限：'))
hi=int(input('上限：'))
for i in range(lo,hi+1):
    if i > 1:
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
            print(i)
