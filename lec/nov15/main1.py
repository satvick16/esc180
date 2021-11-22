# Want to know how efficient the function f is
# For an input of size n, in the worst case, what is the runtime of f proportional to for large n

def f(L):
    # const1
    if L[0] == 5:
        return

    # const2 * len(L) * len(L)//2
    for i in range(len(L)):
        for j in range(len(L)//2):
            print("hi")  # const2

# Runtime: const1 + const2 * len(L) * len(L)//2
#            cons1 + (const2/2)*n^2 (n=len(L))
# O(n^2)

# Pythagorean triple:
# i, j, k s.t. i^2 + j^2 = k^2
# For example, 3, 4, 5
# Want to find a  triple such that i^p + j^p = k^p for some p


def fermat(p):
    n = 1

    while True:
        for i in range(1, n):
            for j in range(1, n):
                for k in range(1, n):
                    if i**p + j**p == k**p:
                        return i, j, k
        n += 1

# Fermat's Last Theorem:
# i**p + j**p == k**p has no int solns for p > 2
