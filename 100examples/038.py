mat=[[1,2,3],
     [3,4,5],
     [4,5,6]
    ]
res=0
for i in range(len(mat)):
    res+=mat[i][i]
print(res)
