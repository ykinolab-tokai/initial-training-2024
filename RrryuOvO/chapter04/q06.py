import math  # exp を呼び出すために math モジュールをインポート

def f(x):
    return math.exp(x)

def dfdx_approx(x):
    dh = 0.0001
    return (f(x + dh) - f(x)) / dh

for x in range(-3, 4):
    fx = f(x)
    dfdx = dfdx_approx(x)
    print(x, fx, dfdx)

def g(x):
    return math.log(x)

def dgdx_approx(x):
    dh = 0.0001
    return (g(x + dh) - g(x)) / dh

for x in [0.25,0.5,1,2,4,8]:
    gx = 1/x
    dgdx = dgdx_approx(x)
    print(x, gx, dgdx)