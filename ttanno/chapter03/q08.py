"""
NumPyの関数 np.log, np.log2, np.log10 を用いて，それぞれの関数のグラフを同じ平面上にプロット（画面に表示，または画像として保存）してください．
ただし， xの範囲は 0.01から 5までとしてください．
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.01,5,100)
log = np.log(x)
log2 = np.log2(x)
log10 = np.log10(x)

plt.plot(x,log,label = "np.log")
plt.plot(x,log2,label = "np.log2")
plt.plot(x,log10,label = "np.log10")
plt.legend()
plt.show()