for p in range(2, 101):
    i = 0
    if p >= 2:
        for k in range(2, p-1):
            if k >= 2:
                a = p % k
                if a != 0:
                    i += 1
                    if i == p-3:
                        print(p)
