def print_matrix_dim(M):
    print(str(len(M)) + "x" + str(len(M[0])))


def dot(v1, v2):
    res = 0

    for e in range(len(v1)):
        res += v1[e] * v2[e]

    return res


def mult_m_v(M, v):
    res = [0 for i in range(len(M))]

    for i in range(len(M)):
        res[i] = dot(v, M[i])

    return res


def matrix_multiplication(m1, m2):
    res = [[0 for i in range(len(m2[0]))] for j in range(len(m1))]

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            col = []

            for k in range(len(m2)):
                col.append(m2[k][j])

            res[i][j] = dot(m1[i], col)

    return res


a = [[1, 2, 3], [4, 5, 6]]
b = [[10, 11], [20, 21], [30, 31]]

print(matrix_multiplication(a, b))
