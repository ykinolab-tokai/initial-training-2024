"""
0度から360度まで1度刻みの三角関数の値をまとめた三角関数表を画面に出力するプログラムを作成してください．
三角関数表は，例えば以下のようなものになります
"""
import numpy as np
theta = np.arange(0, 361, 1)
theta = np.radians(theta)

sin = np.sin(theta)
cos = np.cos(theta)
tan = np.tan(theta)

table = np.array([theta, sin, cos, tan]).T

print(table)