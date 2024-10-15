a=[4, 8, 3, 4, 1]

b = [a[i]%2 for i in range(len(a))]
print(b)

c = [(b[j]+1)%2 for j in range(len(b))]
print(c)

d = [a[k] for k in range(len(a)) if a[k]%2 == 1]
print(d)

