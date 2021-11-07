L = [5, 6, 7, 1, 8, 7, 6]

L[1:4:1]  # [6, 7, 1]
L[5:]  # [7, 6]
L[5::-2]  # [7, 1, 6]

L[::-1]  # reverse
L[:]  # shallow copy

###############################

L[[1, 2], [3, 4]]

L1 = L  # L1 points to same memory address as L
L1 = L[:]  # L1 = [L[0], L[1]] --> 1D list, so defaults to deep copy
L1 = []

# deep copy
for sublist in L:
    L1.append(sublist[:])

###############################
