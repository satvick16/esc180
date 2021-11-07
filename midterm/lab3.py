def sum_cubes(n):
    total = 0

    for i in range(1, n+1):
        total += i ** 3

    return total


def better_sum_cubes(n):
    return n**2 * (n+1)**2 / 4


def check_sum(n):
    return sum_cubes(n) == better_sum_cubes(n)


def check_sums_up_to_n(N):
    for i in range(1, N+1):
        if sum_cubes(i) != better_sum_cubes(i):
            return False

    return False


def pi(n):
    total = 0

    for i in range(n+1):
        total += (-1)**n / (2*n+1)

    return total * 4
