import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    K = int(input())
    file = list(map(int, input().split()))
    sum_file = [0] * (K + 1)
    dp = [[0] * (K + 1) for _ in range(K + 1)]

    for i in range(1, K + 1):
        sum_file[i] = sum_file[i - 1] + file[i - 1]

    for i in range(1, K):
        for j in range(1, K - i + 1):
            dp[j][i+j] = float('inf')
            for k in range(j, i + j):
                dp[j][i + j] = min(dp[j][i + j], dp[j][k] + dp[k + 1][i + j] + sum_file[i + j] - sum_file[j - 1])
    # print(dp)

    print(dp[1][K])