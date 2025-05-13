import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
arr.append(0)

pre_idx = 0
pre_n = arr[0]
next_n = float("inf")
next_idx = 0

for idx in range(N-1):
    if arr[idx] < arr[idx+1]:
        pre_idx = idx
        pre_n = arr[pre_idx]


for idx in range(pre_idx+1, N):
    if arr[idx] > pre_n and arr[idx] == min(arr[idx], next_n):
        next_n = arr[idx]
        next_idx = idx

arr[pre_idx], arr[next_idx] = arr[next_idx], arr[pre_idx]
temp = arr[pre_idx+1:N]
temp.sort()

arr = arr[:pre_idx+1] + temp

if pre_idx >= next_idx: print(-1)
else: print(*arr)