a = 1.2 + 3.8 
#予想　値：5.0　型：float
print(a)
print(type(a))
b = 10 // 100
#予想　値：0　型：int
print(b)
print(type(b))
c = 1 >= 0
#予想　値：True　型：bool
print(c)
print(type(c))
d = 'Hello World' == 'Hello World'
#予想　値：True　型：bool
print(d)
print(type(d))
e = not 'Chainer' != 'Tutorial'
#予想　値：False　型：bool
print(e)
print(type(e))
f = all([True, True, False])
#予想　値：False　型：bool
print(f)
print(type(f))
g = any([True, True, False])
#予想　値：True　型：bool
print(g)
print(type(g))
h = abs(-3)
#予想　値：3　型：int
print(h)
print(type(h))
i = 2 // 0
#予想　2を0で割ることができないのでエラーが起こる。
print(i)
print(type(i))