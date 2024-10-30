
def matrix_sum(X, Y):
    b = [0] * len(X[0])
    c = [0] * len(X[0])
    for i in range(len(X[0])):
        b[i] = X[0][i] + Y[0][i]
        c[i] = X[1][i] + Y[1][i]
    d = [b, c]
    return d

X = [[1, 2, 3],
    [4, 5, 6]]

Y = [[8, 1, 2],
    [-1, 0, -2]]
answer = matrix_sum(X, Y)
print(answer) 