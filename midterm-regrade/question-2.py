M1 = {(0, 0): 5, (1, 2): 1}
M2 = {(0, 0): 5, (1, 2): 1}


def add_sparse_matrices(A, B, dim):
    new = [[0 for i in range(dim[1])] for j in range(dim[0])]

    for d in [A, B]:
        for key, value in d.items():
            new[key[0]][key[1]] += value

    return new


new = add_sparse_matrices(M1, M2, (2, 3))

print(new)
