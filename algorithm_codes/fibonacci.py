# fibonacci function
def fib(n):
    if (n <= 1):
        return n
    return fib(n - 1) + fib(n - 2)


def dp_fib(n):
    f = []
    for i in range(n):
        if (i == 0):
            f.append(0)
        elif (i == 1):
            f.append(1)
        else:
            f.append(f[i - 1] + f[i - 2])
        print(i, f[i])
    print(f)

# fib(10)
dp_fib(10)