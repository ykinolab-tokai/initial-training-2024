#0度から360度まで1度刻みの三角関数の値をまとめた三角関数表を画面に出力するプログラムを作成してください．

import numpy as np
import matplotlib.pyplot as plt



for i in range(0,361,1):
    rad= np.radians(i) #角度をradに変換
    sin= np.sin(rad)
    cos= np.cos(rad)
    tan= np.tan(rad)

    print(f'θ[°]:{i} sinθ {sin:.5f} cosθ {cos:.5f} tanθ{ tan:.5f}')
    print("-"*36)