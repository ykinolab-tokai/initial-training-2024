import numpy as np

A = np.array([[2, -1],[1, 1]])
x = np.array([[1],[1]])
b = np.array([[1],[2]])

dotAx = np.dot(A, x)
answer = dotAx - b
print(answer)
