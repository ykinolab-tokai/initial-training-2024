for p in range(2, 101):
    for k in range(2, p-1):
        if p % k == 0:
            break
    else:
        print(p)
