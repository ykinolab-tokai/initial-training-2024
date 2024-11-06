import numpy as np

#5*4のnumpy配列を作成
array_random = np.random.uniform(0, 100, (5, 4)).astype(int)
print("\n5*4のnumpy配列を作成:\n", array_random)

# 2行3列の要素を取得
element_2_3 = array_random[2, 3]
print("2行3列の要素:", element_2_3)

# 第2列の要素すべてを取得
column_2 = array_random[:, 2]
print("第2列の要素すべて:", column_2)

# 奇数番目の行（1行目、3行目、5行目）の要素すべてを取得
odd_rows = array_random[1::2, :]
print("奇数番目の行の要素すべて:\n", odd_rows)