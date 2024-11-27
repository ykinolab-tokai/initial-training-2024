for p in range(2,101):
    for k in range(2,p):
        if p % k == 0:
            break
    else:
        print(p)