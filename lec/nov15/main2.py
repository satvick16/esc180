# Recursion: functions that call themselves

def factorial(n):
    # base case
    if n <= 1:
        return 1
    else:
        # recursive step
        return n * factorial(n-1)


print(factorial(998))


# def fact(n):
#     F = [0 for i in range(n)]
#     F[0] = 1
#     F[1] = 1

#     for i in range(2, n):
#         F[i] = i * F[i-1]

#     return F[-1]


# print(fact(9999))

def is_winning_sum(s):
    '''Plays the game 21'''
    # base case
    if s == 21:
        return True

    moves = [1, 2]

    for move in moves:
        if is_winning_sum(s + move):
            return False

    return True


def p2(n):
    if n == 21:
        return True

    for move in [1, 2]:
        if p1(n + move):
            return False

    return True


def p1(n):
    if n == 21:
        return True

    for move in [1, 2]:
        if p2(n + move):
            return False

    return True


for i in range(1, 21):
    print(p1(i), is_winning_sum(i))
