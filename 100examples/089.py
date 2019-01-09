n=input()
n = str(n)
a=[]
for i in range(4):
    a.append((int(n[i])+5)%10)
a[0],a[3]=a[3],a[0]
a[1],a[2]=a[2],a[1]
print ("".join('%s' %s for s in a))
