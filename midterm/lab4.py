def count_evens(L):
    total = 0

    for e in L:
        if e % 2 == 0:
            total += 1

    return total


def list_to_str(lis):
    string = "["

    for i in range(len(lis) - 1):
        string += lis[i] + ", "

    string += lis[-1] + "]"

    return string


def lists_are_the_same(list1, list2):
    if len(list1) != len(list2):
        return False

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False

    return True


def simplify_fraction(n, m):
    for i in range(min(n, m), 2, -1):
        if n % i == 0 and m % i == 0:
            n /= i
            m /= i
            break

    print(f"{n}/{m}")


def pi(n):
    total = 0

    for i in range(n+1):
        total += (-1)**n / (2*n+1)

    return total * 4


def leibniz(n):
    import math

    pi_n = int(math.pi * (10**n))

    counter = 0

    while True:
        x = pi(counter)
        if int(x * (10**n)) == pi_n:
            return counter
