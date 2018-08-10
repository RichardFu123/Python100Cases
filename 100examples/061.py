def generate(numRows):
    r = [[1]]
    for i in range(1,numRows):
        r.append(list(map(lambda x,y:x+y, [0]+r[-1],r[-1]+[0])))
    return r[:numRows]
a=generate(10)
for i in a:
    print(i)
