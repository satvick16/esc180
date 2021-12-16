def fib(n):
    if n <= 2:
        return 1

    return fib(n-1) + fib(n-2)

# number of calls = 1 + calls(n-1) + calls(n-2) - fib(n) = O(phi^n)
# above code has double counting
# this can be fixed via caching (memoization)
# base case is stored in default argument


def fib2(n, cache={1: 1, 2: 1}):
    if n in cache:
        return cache[n]
    else:
        cache[n] = fib(n-1) + fib(n-2)
        return cache[n]

# fib(n-1) + fib(n-2) is used O(n) times
# each call produced two calls (see calls diagram w/ ladder pattern)
# approx 2*n calls, approx n additions
# in total, O(n) since fib(n) is called only once for each n
