import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))

cmp = [*arr]

for idx in range(N-2, -1, -1):
    cmp[idx] = max(cmp[idx], cmp[idx+1])

ans = 0

for idx in range(N):
    ans += (cmp[idx] - arr[idx])

print(ans)