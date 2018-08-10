li=[3,2,5,7,8,1,5]

li[-1],li[li.index(min(li))]=li[li.index(min(li))],li[-1]

m=li[0]
ind=li.index(max(li))
li[0]=li[ind]
li[ind]=m

print(li)
