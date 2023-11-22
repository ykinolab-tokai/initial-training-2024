import numpy as np

#すべての要素が0
a = np.zeros((3, 3))
print(a)

#すべての要素が1
b = np.ones((3, 3))
print(b)

#-1から1の間のランダムな要素
c = np.random.random((3, 3))
print(c)

#対角の要素（0行0列成分、1行1列成分、2行2列成分）が2で、他の要素が0
d1 = np.eye(3)
d2 = np.eye(3)
d = d1 + d2
print(d)
