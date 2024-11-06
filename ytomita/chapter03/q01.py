#NumPy配列を np.array([1, 2, 3, 4, 5]) として作成し，作成したNumPy配列の dtype, shape を表示するプログラムを作成してください．
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print(f"dtype:{a.dtype},shape{a.shape}")
#解説
#dtype:Numpy配列のデータ型のこと→配列内の要素の型を示す
# shape:Numpy配列の形状のこと→配列の次元ごとのサイズを表すタプル。各次元の長さ（要素数）を示す
#例:
#1次元配列 np.array([1, 2, 3, 4, 5]) の shape は (5,)
#2次元配列 np.array([[1, 2], [3, 4], [5, 6]]) の shape は (3, 2)（3行2列）