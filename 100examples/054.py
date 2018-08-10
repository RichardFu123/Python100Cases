a=int(input('输入一个数字: '))
b=0                 #     0
b=~b                #     1
b=b<<4              # 10000
b=~b                #  1111
c=a>>4
d=c&b
print('a:',bin(a))
print('b:',bin(b))
print('c:',bin(c))
print('d:',bin(d))

