def sosu(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prints = [x for x in range(2,101) if sosu(x)]
print(prints)
