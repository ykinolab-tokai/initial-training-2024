#NumPyの関数 np.log, np.log2, np.log10 を用いて，それぞれの関数のグラフを同じ平面上にプロット（画面に表示，または画像として保存）してください．ただし，xの範囲は0.01から5までとしてください

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.01, 5, 100)# 0.01 から 5 までの範囲を 100 等分した1次元配列
y1 = np.log(x)
y2 = np.log2(x)
y3 = np.log10(x)
plt.plot(x,y1,label='np.log')
plt.plot(x,y2,label='np.log2')
plt.plot(x,y3,label='np.log10')
plt.legend()
plt.show()