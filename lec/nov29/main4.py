L = [5, 6, 7]

[[], [5], [6], [7], [5, 6], [5, 7], [6, 7], [5, 6, 7]]

# for the list, [5, 6, 7]
# find all subsets of [6, 7] (all0)
# and append 5 to each


def get_all_subsets(L):
    if len(L) == 0:
        return [[]]

    all0 = get_all_subsets(L[1:])

    res = []

    for subset in all0:
        res.append([L[0]] + subset)

    res.extend(all0)

    return res


print(get_all_subsets([1, 2, 3, 4, 5, 6, 7, 8, 9]))
