"""
y=2^xのグラフとy=2^(−x)のグラフを，同じ平面上にプロット（画面に表示，または画像として保存）してください．ただし，
xの範囲は−2までとしてください．
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)
y = 2 ** x 
plt.plot(x, y)

y = 2 ** (-x)
plt.plot(x, y)

plt.savefig("./syamashita/chapter03/q07.jpg")