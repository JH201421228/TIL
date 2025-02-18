import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, K = map(int, input().split())
numbers = [0] * (N+1)

ans = []

for idx in range(N):
    if K < N-idx-1:
        ans.append(K+1)
        numbers[K+1] = 1
        break
    else:
        ans.append(N-idx)
        numbers[N-idx] = 1
        K -= (N-idx-1)

for n in range(1, N+1):
    if not numbers[n]:
        ans.append(n)

print(*ans)