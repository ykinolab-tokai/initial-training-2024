#NumPy配列を np.array([1, 2, 3, 4, 5]) として作成し，作成したNumPy配列の dtype, shape を表示するプログラムを作成してください

import numpy as np

a = np.array([1,2,3,4,5])
print(a.shape)#要素数と次元数を表示
print(a.dtype)#データの型を表示