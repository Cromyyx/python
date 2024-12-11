def fib_tail_rec(n, acc_a=0, acc_b=1):
    if n == 0:
        return acc_a
    elif n == 1:
        return acc_b
    else:
        return fib_tail_rec(n-1, acc_b, acc_a + acc_b)


print(fib_tail_rec(10))
