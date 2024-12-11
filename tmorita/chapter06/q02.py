#NumPyを⽤いてを計算するプログラムを作成してください
import numpy as np

# 行列とベクトルの定義
A = np.array([[2, -1], [1, 1]])  # 行列 A
x = np.array([1, 1])             # ベクトル x
b = np.array([1, 2])             # ベクトル b

# Ax を計算
Ax = np.dot(A, x)

# Ax - b を計算
result = Ax - b

# 結果を表示
print("Ax:", Ax)
print("Ax - b:", result)
