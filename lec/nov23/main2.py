# Mergesort
def merge(L1, L2):
    '''Return the sorted version of L1+L2, 
    assuming that L1 and L2 are sorted in 
    non-decreasing order'''

    # count the total number of append operations
    # each append operation costs c1 time
    # total runtime = c1 * (len(L1) + len(L2))

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


def merge_sort(L):
    if len(L) <= 1:
        return L[:]

    mid = len(L) // 2

    # housekeeping + merge + slicing
    # c3 + c1*len(L) + c2*len(L)
    return merge(merge_sort(L[:mid]), merge_sort(L[mid:]))

# log_2(n) levels
# total runtime = log_2(n)*(c1+c2)*n + (1+2+4+...+n)*c3 = O(nlogn)
