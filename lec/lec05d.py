def artsci_math(arg1, arg2, op):
    '''Return arg1 op arg2, where arg1 and arg2 are 
    numbers and op is one of + or -
    if op is neither + or -, print error message'''

    if op == "+":
        return arg1 + arg2
    elif op == "-":
        return arg1 - arg2
    else:
        print("I am an artsci, I don't know ops that are not + or -")
        # return None


def artsci_math2(arg1, arg2, op):
    if op != "+" and op != "-":
        return None

    if op == "+":
        return arg1 + arg2
    elif op == "-":
        return arg1 - arg2


if __name__ == '__main__':
    print(artsci_math(4, 5, "+"))
    res = artsci_math2(4, 5, "*")

    if res != None:
        print(res)
    else:
        print("The artsci had a hard time")
