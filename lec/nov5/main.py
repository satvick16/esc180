# Counting Sort: Bucket Sort with bucket size 1


def counting_sort(L):
    # n = len(L), m = max(L)

    max_int = max(L)  # O(n), time k1*n
    counts = [0] * (1 + max_int)  # O(m), time k2*m

    for e in L:
        counts[e] += 1  # O(n), time k3*n

    res = []
    for i in range(len(counts)):  # k4*m + k5*m
        res.extend([i] * counts[i])

    return res

# Total time: (k1+k3+k5)*n + (k2+k4)*m
#             O(n+m)
# If we know that max_int is limited, O(n+m) is just O(n)

x = [5, 2, 2, 10, 3]

print(counting_sort(x))
