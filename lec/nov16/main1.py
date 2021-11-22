def print_list(L):
    if len(L) == 1:
        print(L[0])
        return

    print(L[0])
    print_list(L[1:])

# total number of calls = n = len(L)
# runtimes in each call = k1*(n-1) + k2,
#                         k1*(n-2) + k2,
#                         k1*(n-3) + k2
# total runtime
# = n*k2 + k1*(1+2+3+...+(n-1))
# = k2*n + k1(n*(n-1)/2)
# = O(n^2)


def print_list3(L, start, end):
    # same as above but new lists are not created
    if start == end:
        print(L[start])
        return

    print(L[start])
    print_list3(L, start+1, end)

# total runtime = O(n), n = len(L)


def print_list_rev(L):
    if len(L) == 1:
        print(L[0])
        return

    print_list_rev(L[1:])
    print(L[0])


def sum_list(L):
    if len(L) == 0:
        return 0
    return L[0] + sum_list(L[1:])


def sum_list2(L):
    # runtime = c2 + c1 * len(L)
    if len(L) == 0:
        return 0
    if len(L == 1):
        return L[0]

    mid = len(L) // 2
    return sum_list2(L[:mid]) + sum_list2(L[mid:])

# total number of calls = 1   + 2   + 4   + ... + 2^k
#                       = 1   + 2   + 4   + ... + n
#                       = 2^0 + 2^1 + 2^2 + ... + 2^log_2(n)

#                       = (2^(log_2(n) + 1) - 1) / (2 - 1)
#                       = 2*n - 1

# runtime:
# (different calls take different amounts of time)
# (c2 + c1*n) + (2*c2 + c1*n) + (4*c2 + c1*n) + ... + (n*c2 + c1*n)
# c2*(1 + 2 + 4 + ... + 2^log_2(n)) + c1*n*(log_2(n) + 1)
# c2*(2n - 1)                       + c1*n*(log_2(n) + 1)
# n + n*logn
# O(n*logn)
