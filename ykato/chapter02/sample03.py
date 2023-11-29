for p in range(101):
    i = 0
    if p >= 2:
        for k in range(p-1):
            if p >= 2 and p <= 4:
                a = p % k
                if a != 0:
                    i += 1
                    if i == p-3:
                        print(p)
            elif k >= 1:
                a = p % k
                if a != 0:
                    i += 1
                    if i == p-3:
                        print(p)
