# Stirling's approximation: n! = sqrt(2*pi*n) * (n/e)^n
# logn! = log(sqrt(2*pi*n)) + nlogn - nloge = O(nlogn)

# If sorting algorithm is based on comparisons, nlogn is the best possible time complexity
def merge(L1, L2):
    i, j = 0, 0
    merged = []

    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged.append(L1[i])
            i += 1
        else:
            merged.append(L2[j])
            j += 1

    merged.extend(L1[i:])
    merged.extend(L2[j:])

    return merged


L = [1, 2, 10, 3, 4, 5, 2, 3]


def merge_sort(L):
    step = 2
    while step <= len(L):
        for i in range(0, len(L), step):
            begin = i
            end = i + step
            mid = i + step//2
            L[begin:end] = merge(L[begin:mid], L[mid:end])
        step *= 2

    return L


print(merge_sort(L))
