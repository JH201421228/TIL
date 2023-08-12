def sq_func(n):
    if n == 1:
        return 3
    else:
        return (sq_func(n-1)) + (sq_func(n-1) - 1)

print((sq_func(int(input()))) ** 2)