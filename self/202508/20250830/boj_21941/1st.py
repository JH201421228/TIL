import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    S = input().rstrip()

    removable = {}

    for _ in range(int(input())):
        s, score = input().rstrip().split()

        removable[s] = int(score)

    dp = [0] * (len(S)+1)
    dp[0] = 0

    for i in range(1, len(S)+1):
        dp[i] = dp[i-1]+1

        for j in range(1, 101):
            if i-j >= 0:
                temp = S[i-j:i]

                if temp in removable:
                    dp[i] = max(dp[i], dp[i-j] + removable[temp])
            else:
                continue

    print(dp[-1])

    return


if __name__ == "__main__":
    solve()