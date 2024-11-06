#以下の要素を持つ 3×3 のNumPy配列を作成するプログラムを作成してください．
#すべての要素が0
import numpy as np
zero = np.zeros((3,3))
print(zero)
#すべての要素が1
one = np.ones((3,3))
print(one)
#-1から1の間のランダムな要素
import random
three_on_three = np.random.uniform(-1,1,(3,3))
print(three_on_three)
#対角の要素（0行0列成分，1行1列成分，2行2列成分）が2で，他の要素が0
diagonal = np.diag([2,2,2])
print(diagonal)
#解説
#np.zeros((3, 3)): すべての要素が0の3×3行列を作成。
#np.ones((3, 3)): すべての要素が1の3×3行列を作成。
#np.random.uniform(-1, 1, (3, 3)): -1から1の間(浮動小数点数)のランダムな要素を持つ3×3行列を作成。
#np.diag([2, 2, 2]): 対角要素が2の行列を作成。