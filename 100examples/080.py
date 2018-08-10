if __name__ == '__main__':
    i = 0
    j = 1
    x = 0
    while (i < 5) :
        x = 4 * j
        for i in range(0,5) :
            if(x%4 != 0) :
                break
            else :
                i += 1
            x = (x/4) * 5 +1
        j += 1
    print(x)

    for p in range(5):
        x=(x-1)/5*4
    print(x)
