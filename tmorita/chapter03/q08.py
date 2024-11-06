#NumPyの関数 np.log, np.log2, np.log10 を用いて，それぞれの関数のグラフを同じ平面上にプロット（画面に表示，または画像として保存）ただし，$x$の範囲は$0.01$から$5$まで

import numpy as np
import matplotlib.pyplot as plt

# x の範囲を 0.01 から 5 まで生成
x = np.linspace(0.01, 5, 100)

# 各対数関数の値を計算
y_log = np.log(x)      # 自然対数
y_log2 = np.log2(x)     # 2を底とする対数
y_log10 = np.log10(x)   # 10を底とする対数

# グラフのプロット
plt.figure(figsize=(8, 6))
plt.plot(x, y_log, label=r"$y = \ln(x)$", color="blue")
plt.plot(x, y_log2, label=r"$y = \log_2(x)$", color="red", linestyle="--")
plt.plot(x, y_log10, label=r"$y = \log_{10}(x)$", color="orange", linestyle=":")

# グラフの設定
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graphs of $y = \ln(x)$, $y = \log_2(x)$, and $y = \log_{10}(x)$")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)

# グラフを表示
plt.savefig('/home/tomo/initial-training-2024/tmorita/chapter03/q08.jpg')
