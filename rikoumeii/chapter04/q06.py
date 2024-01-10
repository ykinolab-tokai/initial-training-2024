import math  # exp を呼び出すために math モジュールをインポート
import numpy as np
def f(x):
    return math.exp(x)

def dfdx_approx(x):
    dh = 0.0001
    return np.array([(f(xi + dh) - f(xi)) / dh for xi in x])

x = np.arange(-3, 4, 1)
print(dfdx_approx(x))
print()

def d(x):
    return math.log(x)

def dgdx_approx(x):
    dh = 0.0001
    return np.array([(f(xi + dh) - f(xi)) / dh for xi in x])

x = [0.25, 0.5, 1, 2, 4, 8]
for i in range(len(x)):
    y = dgdx_approx(x)
    print(y[i])
