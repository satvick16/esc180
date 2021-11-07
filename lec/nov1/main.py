# In the worst-case, what will the runtime be proportional to?

def longest_run1(s, c):
    run = 0
    max_run = 0

    if c == "z":
        s += "y"
    else:
        s += "z"

    for ch in s:
        if ch != c:
            max_run = max(run, max_run)
            run = 0
        else:
            run += 1

    return max_run

# Runtime: const1 + len(s) * const2
#          O(n), n = len(s)

#################################################

# hard to analyze complexity


def longest_run2(s, ch):
    for longest in range(len(s), -1, -1):
        if ch*longest in s:
            return longest
    return 0


def longest_run3(s, ch):
    # runs at most len(s)+1 times
    for longest in range(len(s), -1, -1):
        cur_run = 0
        # runs at most len(s) times
        for i in range(len(s)):
            # const
            if s[i] == ch:
                cur_run += 1
            else:
                cur_run = 0
            if cur_run == longest:
                return longest
    return 0

# Runtime: (n+1)*n*const
#          cost*n^2 + const*n
#          O(n^2)
