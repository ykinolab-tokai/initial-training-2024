"""
y=2^xのグラフと y=2^−xのグラフを，同じ平面上にプロット（画面に表示，または画像として保存）してください．
ただし， xの範囲は −2から 2までとしてください．
"""
import numpy as np
import matplotlib.pyplot as plt 

x  = np.linspace(-2, 2, 100)
y1 = 2 ** x 
y2 = 2 ** (-x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.show()