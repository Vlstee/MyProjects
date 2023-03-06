def fib(n):
    f1, f2 = 0, 1
    for i in range(2, n):
        f1, f2 = f2, f1+f2
    return f2

print(fib(9))