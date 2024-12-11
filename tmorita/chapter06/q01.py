#(1) 2つのベクトル ,  を受け取り、その和  を返す関数を書いて下さい
def vector_sum(x, y):
    return [x[i] + y[i] for i in range(len(x))]

x = [1, 2, 3]
y = [8, 1, 2]
answer = vector_sum(x, y)
print(answer)  # => [9, 3, 5]

#(2) 2つの⾏列 ,  を受け取り、その和  を返す関数を書いて下さい
def matrix_sum(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

X = [[1, 2, 3], [4, 5, 6]]
Y = [[8, 1, 2], [-1, 0, -2]]
answer = matrix_sum(X, Y)
print(answer)  # => [[9, 3, 5], [3, 5, 4]]


#(3) ⾏列  とベクトル  を受け取り、その積  を返す関数を書いて下さい
def matrix_vector_product(X, y):
    return [sum(X[i][j] * y[j] for j in range(len(y))) for i in range(len(X))]

X = [[1, 2, 3], [4, 5, 6]]
y = [8, 1, 2]
answer = matrix_vector_product(X, y)
print(answer)  # => [16, 49]

#(4) 2つの⾏列 ,  を受け取り、その積  を返す関数を書いて下さい
def matrix_product(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]

X = [[1, 2, 3], [4, 5, 6]]
Y = [[8, 1], [-1, 0], [0, 1]]
answer = matrix_product(X, Y)
print(answer)  # => [[6, 4], [27, 10]]

#(5) ⾏列  を受け取り、その転置  を返す関数を書いて下さい。NumPy等のライブラリは利⽤しないでください
def matrix_transpose(X):
    return [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

X = [[1, 2, 3], [4, 5, 6]]
answer = matrix_transpose(X)
print(answer)  # => [[1, 4], [2, 5], [3, 6]]
