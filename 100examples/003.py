n=0
while (n+1)**2-n*n<=168:
    n+=1

for i in range((n+1)**2):
    if i**0.5==int(i**0.5)and (i+168)**0.5==int((i+168)**0.5):
        print(i-100)
    
