def age(n):
    if n==1:
        return 10
    return 2+age(n-1)
print(age(5))
