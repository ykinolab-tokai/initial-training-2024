#y = 2^x のグラフと$y = 2^{-x}$のグラフを，同じ平面上にプロット（画面に表示，または画像として保存）ただし，$x$の範囲は$-2$から$2$まで

import numpy as np
import matplotlib.pyplot as plt

# x の範囲を -2 から 2 まで生成
x = np.linspace(-2, 2, 100)

# 関数 y = 2^x と y = 2^-x の値を計算
y_positive = 2**x
y_negative = 2**(-x)

# グラフのプロット
plt.figure(figsize=(8, 6))
plt.plot(x, y_positive, label=r"$y = 2^x$", color="blue")
plt.plot(x, y_negative, label=r"$y = 2^{-x}$", color="red", linestyle="--")

# グラフの設定
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graphs of $y = 2^x$ and $y = 2^{-x}$")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)

# グラフを表示
plt.savefig('/home/tomo/initial-training-2024/tmorita/chapter03/q07.jpg')
