def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

x = power(2, 3)
print x