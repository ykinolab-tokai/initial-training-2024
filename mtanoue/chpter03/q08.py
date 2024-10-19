for i in range(2,100):
    a=True
    for j in range(2,i-1):
        if i%j==0:
            a=False
            break
    if a:
        print(i)
