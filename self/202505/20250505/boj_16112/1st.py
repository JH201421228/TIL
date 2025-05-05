import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
k = 1
ans = 0

for idx in range(1, N):
    if k < K:
        ans += (k*arr[idx])
        k += 1
    else: ans += (K*arr[idx])

print(ans)