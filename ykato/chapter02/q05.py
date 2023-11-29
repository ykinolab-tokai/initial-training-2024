#(1)
a = [x for x in range(100)]
b = map(str, a)
c = " ".join(b)
print(c)

#(2)
a = '{:.8}'.format(1.0 / 7.0)
print(a)
