def power(x, n):
    if n == 0:
        return 1

    return x * power(x, n-1)


def interLeave(L1, L2):
    if len(L1) == 1:
        return [L1[0], L2[0]]
    else:
        res = [L1[0], L2[0]]
        L1.pop(0)
        L2.pop(0)
        res.extend(interLeave(L1, L2))
        return res


def reverse_rec(L, index=0):
    # print(L)
    if len(L) == 1:
        return [L[0]]
    if len(L) == 2:
        return [L[1], L[0]]
    res = [L[-1]]
    res.extend(reverse_rec(L[1:len(L)-1]))
    res.append(L[0])
    return res


def zigzag(L):
    n = len(L)
    if n == 0:
        print("")
    elif n == 1:
        print(L[0])
    elif n == 2:
        print(L[0])
        print(L[1])
    elif n % 2 == 1:
        print(L[n//2])
        res = L[:n//2]
        res.extend(L[n//2+1:])
        zigzag(res)
    else:
        print(L[n//2-1])
        print(L[n//2])
        res = L[:n//2-1]
        res.extend(L[n//2+1:])
        zigzag(res)


def is_balanced(s):
    # print(s)
    if len(s) == 0:
        return True

    first_close = s.find(")")

    if first_close != -1:
        # print(first_close)
        first_open = s.find("(", 0, first_close)
        # print(first_open)
        if first_open != -1:
            return is_balanced(s[first_open+1:first_close] + s[first_close+1:])
        else:
            return False
    elif s.find("(") != -1:
        return False
    else:
        return True


def is_fib(L):
    if len(L) == 0:
        return L == []
    if len(L) == 1:
        return L == [1]
    if len(L) == 2:
        return L == [1, 1]
    if len(L) == 3:
        return L == [1, 1, 2]

    if L[-1] == L[-2] + L[-3]:
        return is_fib(L[:-3])
    else:
        return False


if __name__ == '__main__':
    # print(power(2, 3))
    # print()
    # print(interLeave([1, 2, 3], [4, 5, 6]))
    # print()
    # print(reverse_rec([1, 2, 3, 4, 5]))
    # print(is_balanced(
    #     "(well (I think), recursion works like that (as far as I know)"))
    # zigzag([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(is_fib([]))
