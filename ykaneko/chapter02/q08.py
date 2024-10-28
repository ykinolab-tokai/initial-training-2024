for p in range(2, 101):
    a = True
    for k in range(2,int(p ** 0.5)+1):
        if p % k == 0:
            a = False
            break
    if a:
        print(p)


for p in range(2,101):
    for k in range(2,p):
        if p % k ==0:
            break
    if a:
        print(p)