a = 809
for i in range(10,100):
    b = i * a
    if b >= 1000 and b <= 10000 and 8 * i < 100 and 9 * i >= 100:
        print(b,' = 800 * ', i, ' + 9 * ', i)


for i in range(10,100):
    if 8*i>99 or 9*i<100:
        continue
    if 809*i==800*i+9*i:
        print(i)
        break
