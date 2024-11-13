import numpy as np

a = np.zeros((3, 3))
print("全ての要素が0")
print(a)

b = np.ones((3, 3))
print("全ての要素が1")
print(b)

c = np.random.default_rng()
print("-1から1の間のランダムな要素")
print(c.uniform(-1, 1, (3, 3)))
#c1 = np.random.random(3, 3) * 2 - 1

d1 = np.eye(3)
d2 = np.eye(3)
dsum = d1 + d2
print("対角の要素（0行0列成分，1行1列成分，2行2列成分）が2で，他の要素が0")
print(dsum)
