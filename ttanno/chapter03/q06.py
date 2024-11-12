"""
y=x^3−6x^2+9x−3のグラフをプロット（画面に表示，または画像として保存）してください．
ただし,xの範囲は −5から 5までとしてください．また，この3次関数のグラフを 
x軸方向に-2， y軸方向に 2平行移動した関数を同じ平面上にプロットしてください．
"""

import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(-5, 5, 100)
y1 = x**3 - 6*x**2 + 9*x -3
y2 = (x + 2)**3 - 6 * (x + 2)**2 + 9 * (x + 2) - 3 + 2

plt.plot(x, y1, label="former")
plt.plot(x, y2, label="shifted")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()