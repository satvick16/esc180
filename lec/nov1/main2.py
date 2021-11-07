import time


def f1(x):
    return x * 2


def f2(x):
    return x ** 2


def apply(f, x):
    return f(x)


def sum_all(L):
    s = 0
    for e in L:
        s += e
    return s


def timeit(f, x):
    N = 50

    t0 = time.time()

    for i in range(N):
        f(x)

    t1 = time.time()

    return (t1 - t0) / N
