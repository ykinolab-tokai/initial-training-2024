"""以下の要素を持つ$3 \times 3$のNumPy配列を作成するプログラムを作成してください．

すべての要素が0
すべての要素が1
-1から1の間のランダムな要素
対角の要素（0行0列成分，1行1列成分，2行2列成分）が2で，他の要素が0"""
import numpy as np
a=np.zeros((3,3))
print(a)
b=np.ones((3,3))
print(b)
c=np.random.uniform(-1,1,(3,3))
print(c)
d=np.eye(3)*2
print(d)

