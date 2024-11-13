#NumPyの関数 np.log, np.log2, np.log10 を用いて，それぞれの関数のグラフを同じ平面上にプロット（画面に表示，または画像として保存）してください．
# ただし， x の範囲は 0.01 から 5 までとしてください．

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.01, 5, 100)


y_log = np.log(x)      
y_log2 = np.log2(x)     # 底が2の対数
y_log10 = np.log10(x)   # 底が10の対数

plt.figure(figsize=(4, 3))
plt.plot(x, y_log, label=r"$y = \log(x)$", color="blue")
plt.plot(x, y_log2, label=r"$y = \log_2(x)$", color="red")
plt.plot(x, y_log10, label=r"$y = \log_{10}(x)$", color="green")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()