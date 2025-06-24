import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


MOD = 1_000_000_007

def count_groupings(N, A):
    dp = [0] * (N + 1)
    dp[0] = 1  # nothing grouped yet

    for i in range(N):
        # Case 1: i is the start of a group
        group_end = i + A[i]
        if group_end < N:
            dp[group_end + 1] = (dp[group_end + 1] + dp[i]) % MOD

        # Case 2: i is the end of a group
        group_start = i - A[i]
        if group_start >= 0:
            dp[i + 1] = (dp[i + 1] + dp[group_start]) % MOD

    return dp[N]


def solve():
    N = int(input())
    arr = list(map(int, input().split()))

    print(count_groupings(N, arr))

    return


if __name__ == "__main__":
    solve()