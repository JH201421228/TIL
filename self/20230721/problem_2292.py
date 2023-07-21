def hec_func(n):
    if n == 1:
        return 1
    else:
        return hec_func(n-1) + 6 * (n-1)

n = int(input())
i = 1

while n > hec_func(i):
    i += 1

print(i)