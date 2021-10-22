# fibonacci function
def fib(n):
    if (n <= 1):
        return n
    return fib(n - 1) + fib(fib(n - 2))

'''
def dp_fib(n):
    f[0] = 0
    f[1] = 1
    for (int i == 2; i <= n; i ++):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]
'''