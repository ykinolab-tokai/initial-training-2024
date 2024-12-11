def vector_sum(x, y):
    vectorsum = [0, 0, 0]
    for i in range(len(x)):
        vectorsum[i] = x[i] + y[i]
    return vectorsum

x = [1, 2, 3]
y = [8, 1, 2]
answer = vector_sum(x, y)
print('(1)',answer)


def matrix_sum(X, Y):
    matrixsum = [[0, 0, 0],
                [0, 0, 0]]
    for i in range(2):
        for j in range(3):
            matrixsum[i][j] = X[i][j] + Y[i][j]
    return matrixsum

X = [[1, 2, 3],
    [4, 5, 6]]
Y = [[8, 1, 2],
    [-1, 8, -2]]
answer = matrix_sum(X, Y)
print('(2)',answer)



def matrix_vector_product(X, y):
    matrixvectorproduct = [0, 0]
    for i in range(2):
        for j in range(3):
            matrixvectorproduct[i] = X[i][j] * y[i]
    return matrixvectorproduct

X = [[1, 2, 3],
    [4, 5, 6]]
y = [8, 1, 2]
answer = matrix_vector_product(X, y)
print('(3)',answer)



def matrix_product(X, Y):
    matrixproduct = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(3):
                matrixproduct[i][j] += X[i][k] * Y[k][j]
    return matrixproduct

X = [[1, 2, 3],
    [4, 5, 6]]
Y = [[8, 1],
    [-1, 0],
    [0, 1]]
answer = matrix_product(X, Y)
print('(4)',answer)




def matrix_transpose(X):
    matrixtranspose = [[0, 0],[0, 0],[0, 0]]
    for i in range(2):
        for j in range(3):
            matrixtranspose[j][i] += X[i][j]
    return matrixtranspose

X = [[1, 2, 3],
    [4, 5, 6]]
answer = matrix_transpose(X)
print('(5)',answer)
