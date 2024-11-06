"""
y=x^3−6x^2+9x−3のグラフをプロット（画面に表示，または画像として保存）してください．ただし，xの範囲は−5から5までとしてください．また，この3次関数のグラフをx軸方向に-2，y軸方向に2平行移動した関数を同じ平面上にプロットしてください．
"""
import numpy as np
import matplotlib.pyplot as plt

a, b, c, d = 1, -6, 9, -3

x = np.linspace(-5, 5, 100)
y = a * x**3 + b * x**2 + c * x + d

plt.plot(x, y)


y = a * (x+2)**3 + b * (x+2)**2 + c * (x+2) + d +2
plt.plot(x, y)

plt.savefig("./syamashita/chapter03/q06.jpg")