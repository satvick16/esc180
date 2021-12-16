a = [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]

spacings = []
is_diaphragm = False
counter = 0
for elem in a:
    if not elem:
        if is_diaphragm:
            counter += 1
        else:
            counter = 1
            is_diaphragm = True
    else:
        if is_diaphragm:
            spacings.append(counter)
            counter = 0
            is_diaphragm = False

if counter != 0:
    spacings.append(counter)

print(spacings)
