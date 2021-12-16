def print_all(alphabet, n, start_str=""):
    '''Print all strings over alphabet over alphabet of length n,
    preprending start_str
    >>> print_all("abc", 2, "zz")
    zzaa
    zzab
    zzac
    zzba
    zzbb
    zzbc
    zzca
    zzcb
    zzcc
    '''
    if n == 0:
        print(start_str)
        return

    for letter in alphabet:
        print_all(alphabet, n-1, start_str + letter)


print_all("abc", 100)

# n = length of the string to print
# m = length of the alphabet
# m^n calls
# m*(1 + m + m^2 + m^3 + ... + m^n) = m * (m^(n-1) / (m-1)) = O(m^(n+1))
