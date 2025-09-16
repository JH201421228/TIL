import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def set_dp(l, r, v, cards, dp):
    if l > r: return 0

    if dp[l][r]: return dp[l][r]

    if v:
        dp[l][r] = max(cards[l] + set_dp(l+1, r, 1-v, cards, dp), cards[r] + set_dp(l, r-1, 1-v, cards, dp))
    else:
        dp[l][r] = min(set_dp(l+1, r, 1-v, cards, dp), set_dp(l, r-1, 1-v, cards, dp))

    return dp[l][r]


def solve():
    N = int(input())
    cards = list(map(int, input().split()))
    dp = [[0] * N for _ in range(N)]

    print(set_dp(0, N-1, 1, cards, dp))

    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()