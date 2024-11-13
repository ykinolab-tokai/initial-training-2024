#y=2^xのグラフと y=2^−x のグラフを，同じ平面上にプロット（画面に表示，または画像として保存）してください．
# ただし， x の範囲は −2 から 2 までとしてください．

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)

y_plus = 2**x
y_minus = 2**(-x)

plt.figure(figsize=(4,3))
plt.plot(x, y_plus, label=r"$y = 2^x$", color="blue")
plt.plot(x, y_minus, label=r"$y = 2^{-x}$", color="red")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
