#y = x^3 - 6x^2 + 9x - 3 のグラフをプロット（画面に表示，または画像として保存）してください．ただし，$x$の範囲は$-5$から$5$まで また，この3次関数のグラフを$x$軸方向に-2，$y$軸方向に$2$平行移動した関数を同じ平面上にプロット
import numpy as np
import matplotlib.pyplot as plt

# x の範囲を -5 から 5 まで生成
x = np.linspace(-5, 5, 100)

# 元の関数 y = x^3 - 6x^2 + 9x - 3
y = x**3 - 6 * x**2 + 9 * x - 3

# 平行移動した関数 y_trans = (x + 2)^3 - 6(x + 2)^2 + 9(x + 2) - 3 + 2
x_trans = x + 2
y_trans = x_trans**3 - 6 * x_trans**2 + 9 * x_trans - 3 + 2

# グラフのプロット
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="Original function", color="blue")
plt.plot(x, y_trans, label="Translated function", color="red", linestyle="--")

# グラフの設定
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph of the Function and its Translated Version")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)

# グラフを表示
plt.savefig('/home/tomo/initial-training-2024/tmorita/chapter03/q06.jpg')
