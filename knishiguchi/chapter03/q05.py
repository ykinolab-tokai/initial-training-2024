#0度から360度まで1度刻みの三角関数の値をまとめた三角関数表を画面に出力するプログラムを作成してください

import numpy as np
import matplotlib.pyplot as plt

for i in range(0,361,1):
    rad = i * np.pi/180#度°→ラジアンradに変換
    sin = np.sin(i)#sinの値を求める
    cos = np.cos(i)#cosの値を求める
    tan = np.tan(i)#tanの値を求める

    print(f'θ[°]:{i} sinθ:{sin:.5f} cosθ:{cos:.5f} tanθ:{tan:.5f}')