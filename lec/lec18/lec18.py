L = [[0, 1, 0, 1, 0],
     [0, 0, 0, 0, 5],
     [2, 0, 0, 0, 0]]

# more efficient
M = {(0, 1): 1, (1, 4): 5, (0, 3): 1, (2, 0): 2}

Mdim = (3, 5)

v = [1, 2, 3, 4, 5]


def mult_M_by_v(M, Mdim, v):
    res = [0] * Mdim[0]

    for coords, val in M.items():
        res[coords[0]] += val * v[coords[1]]

    return res

###############################################################


grades = {"PHY": "A+", "CIV": "A", "CSC": "A+", "ESC": "B+"}

del grades["PHY"]

# empty dictionary
grades.clear()

# remove all entries with non-A, non-A+ grades


def correct_transcript_bad(grades):
    for course in grades:
        if grades[course] not in ["A", "A+"]:
            del grades[course]


def correct_transcript_1(grades):
    for course in list(grades.keys()):
        if grades[course] not in ["A", "A+"]:
            del grades[course]


def drop_everything_1(grades):
    while len(grades) > 0:
        del grades[list(grades.keys())[0]]
