import sys
sys.setrecursionlimit(5_000)
sys.stdin = open("input.txt")
input = sys.stdin.readline


MOD = 1_000_000_007


def solve():
    N, K = map(int, input().split())
    
    dp = [[0] * (K+1) for _ in range(2**(N+1)-1)]

    length = 2**(N+1)-1

    for i in range(N, -1, -1):
        cur = 2**(i+1)-1
        dp[cur][0] = 1
        for j in range(1, K+1):
            if cur<<1 < length:
                dp[cur][]
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()