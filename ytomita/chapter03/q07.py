#y=2**xのグラフと y=2**−xのグラフを，同じ平面上にプロット（画面に表示，または画像として保存）してください．
# ただし， xの範囲は −2から2までとしてください．
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2,100,dtype=float)#dtype=float で生成される配列のデータ型を float（浮動小数点数）に指定
y = 2**x
y1 = 2**(-x)

plt.ylim()
plt.plot(x,y,label = "y = 2**x")
plt.plot(x,y1,label = "y = 2**(-x)")
plt.legend()
plt.show()



