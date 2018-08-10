raw=[]
for i in range(3):
    x=int(input('int%d: '%(i)))
    raw.append(x)
    
for i in range(len(raw)):
    for j in range(i,len(raw)):
        if raw[i]>raw[j]:
            raw[i],raw[j]=raw[j],raw[i]
print(raw)


raw2=[]
for i in range(3):
    x=int(input('int%d: '%(i)))
    raw2.append(x)
print(sorted(raw2))
