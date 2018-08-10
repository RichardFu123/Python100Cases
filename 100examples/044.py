X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
 
Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]
 
res=[[0,0,0],
    [0,0,0],
    [0,0,0]]
for i in range(len(res)):
    for j in range(len(res[0])):
        res[i][j]=X[i][j]+Y[i][j]
print(res)
