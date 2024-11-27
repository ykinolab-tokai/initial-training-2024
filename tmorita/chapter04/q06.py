import math

# 数値微分による導関数の近似
def derivative_approx(func, x, dh=0.0001):
    return (func(x + dh) - func(x)) / dh

# 指数関数の定義
def exp_function(x):
    return math.exp(x)

# 対数関数の定義
def log_function(x):
    return math.log(x)

# 確認
x_i = [-3, -2, -1, 0, 1, 2, 3]
x_ii = [0.25, 0.5, 1, 2, 4, 8]

# 指数関数の導関数の数値微分と正確な値の比較
print("i指数関数の導関数の比較:")
for x in x_i:
    approx = derivative_approx(exp_function, x)
    exact = math.exp(x)
    print(f"x = {x}, 数値微分: {approx:.5f}, 正確な値: {exact:.5f}")

# 対数関数の導関数の数値微分と正確な値の比較
print("\nii対数関数の導関数の比較:")
for x in x_ii:
    approx = derivative_approx(log_function, x)
    exact = 1 / x
    print(f"x = {x}, 数値微分: {approx:.5f}, 正確な値: {exact:.5f}")


