i=0
n=0
def dummy():
    i=0
    print(i)
    i+=1
def dummy2():
    global n
    print(n)
    n+=1
print('函数内部的同名变量')
for j in range(20):
    print(i)
    dummy()
    i+=1
print('global声明同名变量')
for k in range(20):
    print(n)
    dummy2()
    n+=10
