total=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if ((i!=j)and(j!=k)and(k!=i)):
                print(i,j,k)
                total+=1
print(total)



import itertools
sum2=0
a=[1,2,3,4]
for i in itertools.permutations(a,3):
    print(i)
    sum2+=1
print(sum2)
