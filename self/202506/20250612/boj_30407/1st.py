import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


# dp[i][j][k] i번째 턴에 j만큼의 거리에서 k 만큼 깜짝놀라게하기를 썻을 때 최소 비용


def solve():
    N = int(input())
    H, D, K = map(int, input().split())
    dp = [[[float("inf")] * 2 for _ in range(N*K+D+1)] for _ in range(N+1)]
    dp[0][D][0] = 0
    damage = [int(input()) for _ in range(N)]

    for i in range(N):
<<<<<<< HEAD
        for
=======
        for j in range(D, N*K+D+1):
            if dp[i][j][0] != float("inf"):
                dp[i+1][j+K][0] = min(dp[i+1][j+K][0], dp[i][j][0] + max(0, damage[i]-j-K))
                dp[i+1][j][0] = min(dp[i+1][j][0], dp[i][j][0] + max(0, (damage[i]-j)//2))
                if i != N-1: dp[i+2][j+K][1] = dp[i][j][0] + max(0, damage[i]-j)
            if dp[i][j][1] != float("inf"):
                dp[i+1][j+K][1] = min(dp[i+1][j+K][1], dp[i][j][1] + max(0, damage[i]-j-K))
                dp[i+1][j][1] = min(dp[i+1][j][1], dp[i][j][1] + max(0, (damage[i]-j)//2))

    min_damage = float("inf")
    for v in dp[-1]:
        min_damage = min(min_damage, min(v))

    ans = H - min_damage
    if ans > 0: print(ans)
    else: print(-1)
>>>>>>> 78b049f72a845b2d10d36ed0505dfd0372b8597a

    return


if __name__ == "__main__":
    solve()