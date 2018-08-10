a=input('被加数字：')
n=int(input('加几次？：'))
res=0
for i in range(n):
    res+=int(a)
    a+=a[0]
print('结果是：',res)
