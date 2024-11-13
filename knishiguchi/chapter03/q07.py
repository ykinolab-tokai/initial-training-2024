#y=2xのグラフとy=2−xのグラフを，同じ平面上にプロット（画面に表示，または画像として保存）してください．ただし，xの範囲は−2から2までとしてください

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100,dtype=float)# -2 から 2 までの範囲を 100 等分した1次元配列
y1 = 2**x
y2 = 2**(-x)

plt.plot(x,y1,label='y = 2 ** x')
plt.plot(x,y2,label='y = 2 ** (-x)')
plt.legend()
plt.show()