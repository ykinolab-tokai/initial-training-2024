print(type(1.2+3.8))
print(type(10//100))
print(type(1>=0))
print(type('Hello World'=="Hello World"))
print(type(not 'Chainer'!='Tutorial'))
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

print(type(all([True,True,False])))

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

print(type(any([True,True,False])))

print(type(abs(-3)))


