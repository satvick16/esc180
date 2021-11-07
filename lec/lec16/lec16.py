# print all strings of length n over the alphabet

def gen_nested_loop(n):
    '''Generate a nested for loop that prints all strings of length n over alphabet
    (alphabet is a global variable)
    '''
    res = "def gen_passwords(alphabet):\n"

    for i in range(n):
        res += " " * (i + 1)
        res += f"for letter{i} in alphabet:\n"

    res += " " * (n + 1)
    res += "print("

    for i in range(n-1):
        res += f"letter{i} + "

    res += f"letter{n-1})\n"
    return res


code = gen_nested_loop(5)
exec(code)
gen_passwords("abcde")

'''
for letter0 in alphabet:
    for letter1 in alphabet:
        ...
        ...
        ...
            print(letter0 + letter1 + letter2...)
'''
