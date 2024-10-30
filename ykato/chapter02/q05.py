#(1)
print("(1)")
a = [(f'{i}') for i in range(100)]
b = map(str, a)
c = " ".join(b)

print (c)

print("(2)")
a = ("{:.8f}".format(1.0 / 7.0))
print(a)
