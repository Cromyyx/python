def sum_(n):
    if n == 0:
        return 0
    else:
        return n+sum_(n-1)


print(sum_(5))
