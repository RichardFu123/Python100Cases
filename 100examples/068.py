from collections import *
li=[1,2,3,4,5,6,7,8,9]
deq=deque(li,maxlen=len(li))
print(li)
deq.rotate(int(input('rotate:')))
print(list(deq))
