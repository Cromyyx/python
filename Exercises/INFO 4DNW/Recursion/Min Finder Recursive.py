field = [5, 3, 8, 7, 2, 4]


def minfinder(field):
    if len(field) == 1:
        return field[0]
    else:
        min_rest = minfinder(field[1:])
        return min(field[0], min_rest)


print(minfinder(field))


