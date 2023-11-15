a = [x for x in range(100)]
b = []
b.append(2)

for x in range(3, len(a)):
    for p in range(2, x):
        if x % p != 0:
            if p == x-1:
                b.addend(x)
            else:
                pass
            else:
                break
print(b)

