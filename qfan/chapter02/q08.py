def sosu(x):
    for j in range(2,x):
        if x %j==0:
            return False
    return True
for i in range(2,100):
    if sosu(i):
        print(i)
