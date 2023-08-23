import sys
sys.stdin = open('input.txt')

Test = int(input())
for test in range(Test):
    N, M, K = map(int, input().split())
    customer_time = list(map(int, input().split()))
    time_line = [0] * (max(customer_time) + 1)

    for i in customer_time:
        time_line[i] -= 1

    for i in range(M, max(customer_time) + 1, M):
        time_line[i] += K

    for i in range(1, max(customer_time)):
        time_line[i+1] += time_line[i]

    for i in time_line:
        if i < 0:
            print(f'#{test+1} Impossible')
            break
    else:
        print(f'#{test+1} Possible')