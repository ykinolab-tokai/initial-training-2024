#以下の要素を持つ 3×3のNumPy配列を作成するプログラムを作成してください．
#1 すべての要素が0
#2 すべての要素が1
#3 -1から1の間のランダムな要素
#4 対角の要素（0行0列成分，1行1列成分，2行2列成分）が2で，他の要素が0

import numpy as np

#1
array_0 =np.zeros((3,3))
print("すべての要素が0\n",array_0)

#2
array_1 =np.ones((3,3))
print("すべての要素が1\n",array_1)

#3
array_random =np.random.uniform(-1,1,(3,3))
print("-1から1の間のランダムな要素\n",array_random)

#4
array_taikaku =np.eye(3)*2
print("対角の要素が2で他の要素が0\n",array_taikaku)

