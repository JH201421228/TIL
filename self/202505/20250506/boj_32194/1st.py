import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
dp = [0, 1]

for _ in range(N):
    q, x, y = map(int, input().split())

    if q == 1:
        if dp[y]-dp[x-1] == y-x+1:
            dp.append(dp[-1]+1)
            print("Yes")
        else:
            dp.append(dp[-1])
            print("No")
    else:
        if dp[y]-dp[x-1] == 0:
            dp.append(dp[-1]+1)
            print("Yes")
        else:
            dp.append(dp[-1])
            print("No")