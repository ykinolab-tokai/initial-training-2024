for p in range(101):
    i = 0
    if p >= 2:
        for k in range(p-1):
            if k >= 1:
                a = p % k
                if a != 0:
                    i += 1
                    if p <= 0 and p >= 4:
                        if i == p-1:
                            print(p)
                    elif i == p-3:
                        print(p)
