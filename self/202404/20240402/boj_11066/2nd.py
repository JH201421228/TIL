import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


for _ in range(int(input())):
    K = int(input())
    K_list = list(map(int, input().split()))
    for idx in range(1, K):
        K_list[idx] += K_list[idx - 1]
    dp = [[0] * K for _ in range(K)]
    for i in range(1, K):
        for j in range(K-i):
            dp[j][i+j] = float('inf')
            for k in range(j, i+j+1):
                dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][i+j] + K_list[j+i] - K_list[j-1])
    print(dp)