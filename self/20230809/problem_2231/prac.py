N = int(input())

ans = 0

for i in range(1, N):
    test_num = i
    sum_num = 0

    while True:

        if test_num < 10:
            sum_num += test_num
            break

        else:
            sum_num += test_num % 10
            test_num = test_num // 10

    if i + sum_num == N:
        ans = i
        break

print(ans)