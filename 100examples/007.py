import copy
a = [1,2,3,4,['a','b']]

b = a

c = a[:]

d = copy.copy(a)

e = copy.deepcopy(a)

a.append(5)
a[4].append('c')

print('a=',a)

print('b=',b)

print('c=',c)

print('d=',d)

print('e=',e)
