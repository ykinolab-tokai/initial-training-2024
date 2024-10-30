for p in range(2,100):
    a=True
    for k in range(2,p-1):
        if p%k==0:
            a=False
            break
    if a:
        print(p)
