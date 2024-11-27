import math  # log を呼び出すために math モジュールをインポート
import numpy as np

def f(x):
    return math.log(x)

def dfdx_approx(x):
    dh = 0.0001
    return (f(x + dh) - f(x)) / dh

x_range = np.array([0.25,0.5,1,2,4,8])

for i in x_range:
    y = 1/i
    diff = dfdx_approx(i)-y
    print(f"{i}:得られた値 {dfdx_approx(i):.7f}, 正確な対数の値{f(i):.7f}, 微分した値{y:.7f}, 差{diff:.7f}")