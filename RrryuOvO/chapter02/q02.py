result = 1.2 + 3.8
print(result, type(result))

result = 10 // 100
print(result, type(result))


result = 1 >= 0
print(result, type(result))


result = 'Hello World' == 'Hello World'
print(result, type(result))


result = not 'Chainer' != 'Tutorial'
print(result, type(result))


result = all([True, True, False])
print(result, type(result))


result = any([True, True, False])
print(result, type(result))


result = abs(-3)
print(result, type(result))


try:
    result = 2 // 0
except ZeroDivisionError as e:
    result = e
print(result, type(result))
