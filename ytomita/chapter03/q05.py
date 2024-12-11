#0度から360度まで1度刻みの三角関数の値をまとめた
# 三角関数表を画面に出力するプログラムを作成してください． 
# 三角関数表は，例えば以下のようなものになります
import numpy as np
import matplotlib.pyplot as pl

for i in range(0,361,1):
    rad = i * np.pi/180#度°→ラジアンradに変換
    sin = np.sin(i)#np.sin():sinの値を求める関数
    cos = np.cos(i)#np.cos():cosの値を求める関数
    tan = np.tan(i)#np.tan():tanの値を求める関数

    print(f"θ[°]:{i} sinθ:{sin:.5f} cosθ:{cos:.5f} tanθ:{tan:.5f}")
