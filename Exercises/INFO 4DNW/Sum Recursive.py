def sum_(n):
    if n == 0:
        return n
    else:
        return n+sum_(n-1)


print(sum_(5))
