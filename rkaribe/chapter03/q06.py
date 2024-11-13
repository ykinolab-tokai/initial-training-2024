#y=x^3−6x^2+9x−3のグラフをプロット（画面に表示，または画像として保存）してください．
# ただし， xの範囲は −5から 5までとしてください．
# また，この3次関数のグラフを x軸方向に-2， y軸方向に 2平行移動した関数を同じ平面上にプロットしてください．

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

y = x**3-6*x**2+9*x-3

x_direction= x + 2
y_direction = x_direction**3 - 6 * x_direction**2 + 9 * x_direction - 3 + 2


plt.figure(figsize=(4, 3))
plt.plot(x, y, label="y_default", color="blue")
plt.plot(x, y_direction, label="y_change", color="red")


plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()