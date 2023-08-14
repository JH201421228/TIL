def plus_func(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return plus_func(n-1) + n

n = int(input())
i = 1
while n > plus_func(i):
    i += 1

num = n - plus_func(i - 1)
if i % 2 == 1:
    print(f'{i + 1 - num}/{num}')
else:
    print(f'{num}/{i + 1 - num}')