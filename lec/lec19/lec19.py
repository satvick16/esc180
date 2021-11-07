# runtime complexity analysis

def find_i(L, e):
    '''Return the index of the first appearance of e in L (and None if e is not in L)'''
    # L.index(e)
    for i in range(len(L)):  # 1 operation
        if L[i] == e:  # 2 operations
            return i  # 1 operation

    return None  # 1 operation

# overall number of operations = 3 * k + 1, where k is the number of times the loop repeats
# worst-case runtime complexity = 3 * n + 1 operations, where n = len(L)

# the runtime will be proportional to 3 * n + 1 seconds (in the worst case)
# the actual runtime (a * (3*n + 1)), where a is the number of ops per second
# the worst case runtime complexity is O(n)

# in general,
# 3n^3-n is O(n^3)
# 5n^7 + n^2 is O(n^2)

# L is sorted


def binary_search(L, e):
    left = 0
    right = len(L) - 1

    while right - left >= 2:
        mid = (left + right) // 2

        if L[mid] == e:
            return mid
        elif L[mid] > e:
            right = mid - 1
        else:
            left = mid + 1

    if L[left] == e:
        return left
    elif L[right] == e:
        return right
    else:
        return None
