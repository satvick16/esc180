# import numpy as np
# from math import acos, degrees


# def angle_between(v1, v2):
#     return acos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))


# print(round(degrees(angle_between([1, 0], [1, 1]))))

#####################################################################

obj = [[1, 2], [[5, 6], 2], [1, [5, 6]]]


def deep_copy(obj):
    '''Return a deep copy of obj
    obj is a list of nested lists that cointain ints or an int'''

    if type(obj) == int:
        return obj

    copy = []

    for elem in obj:
        copy.append(deep_copy(elem))

    return copy

# number of calls = number of distinct objects in obj
# number of copies of ints = number of ints in obj
# Overall complexity = O([# of distinct objects] + [# of distinct ints])
