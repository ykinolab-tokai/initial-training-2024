import math

def f(x):
    return math.exp(x)

def dfdx_approx(x):
    dh = 0.0001
    return (f(x + dh) - f(x)) / dh

print("exp")
for i in range(-3, 4):
    result_exp = f(i)
    print (f'exp({i}): {result_exp}')


print("log")
b = 0.25
for i in range(6):
    result_log = dfdx_approx(b)
    print (f'log({i}): {result_log}')
    b += b
