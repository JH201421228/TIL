import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


S = input().rstrip()

dp = [0] * len(S)
dp[0] = 1

if not int(S[0]):
    print(0)
    sys.exit(0)

if len(S) >= 2:
    if not int(S[1]):
        if int(S[0]) == 1 or int(S[0]) == 2:
            dp[1] = dp[0]
        else:
            print(0)
            sys.exit(0)
    else:
        dp[1] += 1
        if int(S[0]) * 10 + int(S[1]) <= 26:
            dp[1] += 1

for i in range(2, len(S)):
    if not int(S[i]):
        if int(S[i-1]) == 1 or int(S[i-1]) == 2:
            dp[i] = dp[i-2]
        else:
            print(0)
            sys.exit(0)
    else:
        dp[i] = dp[i-1]
        if not int(S[i-1]):
            continue
        elif int(S[i-1]) * 10 + int(S[i]) <= 26:
            dp[i] += dp[i-2]

print(dp[-1] % 1_000_000)