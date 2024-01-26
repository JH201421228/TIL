import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

memo = [0] * (N+1)
ans = [[] for _ in range(N+1)]
ans[1].append(1)

for idx in range(2, N+1):
    memo[idx] = memo[idx-1] + 1
    pre = idx-1
    if not idx % 3 and memo[idx//3]+1 < memo[idx]:
        memo[idx] = memo[idx//3] + 1
        pre = idx//3
    if not idx % 2 and memo[idx//2]+1 < memo[idx]:
        memo[idx] = memo[idx//2] + 1
        pre = idx//2


    ans[idx] = [idx] + ans[pre]

print(memo[N])
print(*ans[N])
