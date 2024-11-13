#y=x**3−6*x**2+9*x−3のグラフをプロット（画面に表示，または画像として保存）してください．ただし，xの範囲は−5から5までとしてください．また，この3次関数のグラフをx軸方向に-2y軸方向に2平行移動した関数を同じ平面上にプロットしてください．
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)# -5 から 5 までの範囲を 100 等分した1次元配列
y = x**3 - 6*(x**2) + 9*x - 3
y1 = (x+2)**3 - 6*(x+2)**2 + 9*(x+2) - 1

plt.plot(x,y)
plt.plot(x,y1)
plt.show()