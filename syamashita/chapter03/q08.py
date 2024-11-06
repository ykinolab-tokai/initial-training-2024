"""
NumPyの関数 np.log, np.log2, np.log10 を用いて，それぞれの関数のグラフを同じ平面上にプロット（画面に表示，または画像として保存）してください．ただし，xの範囲は0.01から5までとしてください．
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.01, 5, 100)
y = np.log(x)
plt.plot(x, y)

y = np.log2(x)
plt.plot(x, y)

y = np.log10(x)
plt.plot(x, y)

plt.savefig("./syamashita/chapter03/q08.jpg")