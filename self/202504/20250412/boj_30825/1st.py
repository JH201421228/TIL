import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, K = map(int, input().split())

arr = list(map(int, input().split()))

acc, pre, n = 0, arr[0], 1

for idx in range(1, N):
    if arr[idx] > pre + K:
        acc += (idx*(arr[idx]-pre-K))
        pre = arr[idx]
    else:
        acc += (pre+K-arr[idx])
        pre += K

print(acc)