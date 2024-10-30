for p in range(2, 101):
    is_prime = True
    for k in range(2, int(p ** 0.5) + 1):
        if p % k == 0:
            is_prime = False
            break
    if is_prime:
        print(p)
