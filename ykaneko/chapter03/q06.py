#y=x^3−6x^2+9x−3のグラフをプロット（画面に表示，または画像として保存）してください．ただし， x の範囲は −5 から 5 までとしてください．また，この3次関数のグラフを x 軸方向に-2， y 軸方向に 2 平行移動した関数を同じ平面上にプロットしてください．
import numpy as np
import matplotlib.pyplot as plt
#Matplotlibを利用してグラフを描画するためにmatplotlib.pyplotモジュールをインポート

x = np.linspace(-5, 5, 100)
#-5から5までの範囲を100等分した配列を作成
y1 = x**3 - 6*x**2 + 9*x - 3
y2 = (x+2)**3 - 6*(x+2)**2 + 9*(x+2) - 3 + 2
#xをx-αに置き換えることでグラフを右にαだけ平行移動できる
#yをy-βに置き換えることでグラフを上にβだけ平行移動できる(-2を右辺に移項)
plt.plot(x,y1,label='y=x^3−6x^2+9x−3')
plt.plot(x,y2,label='y=(x-2)^3 - 6*(x-2)^2 + 9*(x-2) - 3 + 2')
#関数をプロットする。labelでグラフの説明
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
#labelで説明した内容を表示
plt.grid(True)
#目盛り線を表示
plt.show()
#グラフを画面に表示