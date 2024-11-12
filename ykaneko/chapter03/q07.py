#1.	y=2^xのグラフと y=2^−x のグラフを，同じ平面上にプロット（画面に表示，または画像として保存）してください．ただし， x の範囲は −2 から 2 までとしてください．
import numpy as np
import matplotlib.pyplot as plt
#Matplotlibを利用してグラフを描画するためにmatplotlib.pyplotモジュールをインポート
x = np.linspace(-2, 2, 100)
#-2から2までの範囲を100等分した配列を作成
y1 = 2**x
y2 = 2**(-x)
#関数を定義
plt.plot(x,y1,label='y=2^x')
plt.plot(x,y2,label='y=2^(-x)')
#関数をプロットする。labelでグラフの説明
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
#labelで説明した内容を表示
plt.grid(True)
#目盛り線を表示
plt.show()
#グラフを画面に表示