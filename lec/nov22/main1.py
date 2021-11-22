# 2^n = 2^(n-1) * 2

def power2A(n):
    if n == 0:
        return 1

    # log_10(2^(n-1)) decimal digits, runtime = c1*(n-1)
    return 2 * power2A(n-1)

# n+1 calls, but each call takes a different amount of time
# runtime = c1*(1+2+3...+(n-1)) + c2*(n+1)
#         = c1*(n)(n-1)/2 + c2(n+1)
#         = O(n^2)

#####################################################################

# 2^n = 2^(n//2) * 1 if n even and 2^(n//2) * 2 if n odd


def power2B(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2

    half_power = power2B(n // 2)

    if n % 2 == 0:
        return half_power * 1
    else:
        return half_power * 2

# number of calls = log_2(n)
# If the multiplication takes constant time, runtime = O(logn)
# Assume multiplication takes time proportional to number of digits:
# Total runtime = c1*(1+4+8+...+n/2+n) + c2*(log_2(n))
#               = c1*(2n-1) + c2*log_2(n)
#               = O(n)
