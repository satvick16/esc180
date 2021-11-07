import random

# Bogosort


def is_sorted_nondecreasing(L):
    # return L == sorted(L)

    for i in range(len(L) - 1):
        if L[i] > L[i+1]:
            return False

    return True


def bogosort(L):
    while not is_sorted_nondecreasing(L):
        i, j = int(len(L) * random.random()), int(len(L) * random.random())
        L[i], L[j] = L[j], L[i]

    return L


L = [1, 2, 10, 2, 10, 2, 3]
print(bogosort(L))

# There are n! permutations of L
# n! = n*(n-1)*(n-2)*...*1
# The runtime of Bogosort is approximately O(n!)
