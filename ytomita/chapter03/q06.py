#y=x3−6x2+9x−3のグラフをプロット
# （画面に表示，または画像として保存）してください．ただし,xの範囲は 
# −5から 5までとしてください．また，この3次関数のグラフを x軸方向に-2， 
#y軸方向に 2 平行移動した関数を同じ平面上にプロットしてください．
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,100)#-5~5の間を100等している
y = x**3 - 6*(x**2) + 9*x - 3

x1 = x-2
y1 = y+2
plt.xlim(-5,5)
plt.plot(x,y,label = "y = x**3 - 6(x**2) + 9*x - 3")
plt.plot(x1,y1,label = "x = -2,y = 2")
plt.legend()
plt.show()