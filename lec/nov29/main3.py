def all_combinations(alphabet, n, start_str=""):
    '''Return the list of all combinations of length n over the alphabet with start_str prepended

    >>> all_combinations("abc", 2)
    set(['aa', 'ab', 'ac', ...])
    '''
    if n == 0:
        return set([start_str])

    res = []

    for letter in alphabet:
        res.extend(all_combinations(alphabet, n-1, start_str + letter))

    return set(res)


print(all_combinations("abc", 4))
