import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    A = list(map(ord, input().rstrip()))
    B = list(map(ord, input().rstrip()))
    K = int(input())

    dp = [[0] * (len(B)+1) for _ in range(len(A)+1)]
    
    for i in range(1, len(A)+1):
        dp[i][0] = K*i
        for j in range(1, len(B)+1):
            if i == 1: dp[0][j] = K*j
            dp[i][j] = min(dp[i-1][j-1] + abs(A[i-1] - B[j-1]), dp[i][j-1] + K, dp[i-1][j] + K)
    
    print(dp[-1][-1])

    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()