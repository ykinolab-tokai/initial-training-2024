a = 1.2 + 3.8
print("1.2 + 3.8")
a = type(a)
print(a)

b = 10 // 100
print("10 // 100")
b = type(b)
print(b)

c = 1 >= 0
print("1 >= 0")
c = type(c)
print(c)

d = 'Hello World' == 'Hello World'
print("Hello World == Hello World")
d = type(d)
print(d)

e = not 'Chainer' != 'Tutorial'
print("not Chainer != Tutorial")
e = type(e)
print(e)

print("True, True, False")
print(type(all([True, True, False])))

print("True, True, False")
print(type(any([True, True, False])))

print("abs(-3)")
print(type(abs(-3)))

print("2 // 0")
print(type(2 // 0))
