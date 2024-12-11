import math  # exp を呼び出すために math モジュールをインポート

def f(x):
    return math.exp(x)

def dfdx_approx(x):
    dh = 0.0001
    return (f(x + dh) - f(x)) / dh

for i in range(-3,4,1):
    diff = dfdx_approx(i)-f(i)
    print(f"{i}:得られた値 {dfdx_approx(i):.7f},正確な微分の値{f(i):.7f},差{diff:.7f}")