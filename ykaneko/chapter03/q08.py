#1.	NumPyの関数 np.log, np.log2, np.log10 を用いて，それぞれの関数のグラフを同じ平面上にプロット（画面に表示，または画像として保存）してください．ただし， x の範囲は 0.01 から 5 までとしてください．
import numpy as np
import matplotlib.pyplot as plt
#Matplotlibを利用してグラフを描画するためにmatplotlib.pyplotモジュールをインポート
x = np.linspace(0.01, 5, 100)
#0.01から5までの範囲を100等分した配列を作成
y1 = np.log(x)  #自然対数（底e）np.logはlogを計算する関数
y2 = np.log2(x) #底が2の対数    
y3 = np.log10(x)#底が10の対数

plt.plot(x,y1,label='y=log(x)')
plt.plot(x,y2,label='y=log2(x)')
plt.plot(x,y3,label='y=log10(x)')
#関数をプロットする。labelでグラフの説明
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
#labelで説明した内容を表示
plt.grid(True)
#目盛り線を表示
plt.show()
#グラフを画面に表示