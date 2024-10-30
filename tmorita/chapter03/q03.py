import numpy as np

# すべての要素が0の3×3配列
array_zero = np.zeros((3, 3))
print("すべての要素が0:\n", array_zero)

# すべての要素が1の3×3配列
array_one = np.ones((3, 3))
print("\nすべての要素が1:\n", array_one)

# -1から1の間のランダムな要素を持つ3×3配列
array_random = np.random.uniform(-1, 1, (3, 3))
print("\n-1から1の間のランダムな要素:\n", array_random)

# 対角要素が2で他の要素が0の3×3配列
array_diagonal = np.eye(3) * 2
print("\n対角要素が2で他の要素が0:\n", array_diagonal)
