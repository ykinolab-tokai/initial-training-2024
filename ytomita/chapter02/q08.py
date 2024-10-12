for i in range(2,101):
    i = True
    for j in range(2,i):
        if (i%j)== 0:
            i = False
            break
    if i:
        print(i)