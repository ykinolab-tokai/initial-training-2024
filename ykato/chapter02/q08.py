for p in range(2, 101):
    for k in range(2, p-1):
        a = p % k
        if a == 0:
            break
    else:
        print(p)
