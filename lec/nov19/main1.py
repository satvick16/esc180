def fact_while(n):
    i = 1
    prod = 1

    while i != n + 1:
        prod = prod * i
        i += 1

    return prod


def fact_iter(n, prod=1, i=1):
    # recursive analog of fact_while
    if i == n + 1:
        return prod
    else:
        return fact_iter(n, prod*i, i + 1)


def fact(n):
    # fact_iter but backwards (breaking down instead of building up)
    if n <= 1:
        return 1

    return n * fact(n - 1)
