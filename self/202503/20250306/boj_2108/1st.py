import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())

sum_n = 0
max_n = -float("inf")
min_n = float("inf")
nums = [0] * 8_001
k = 0
h = []

for _ in range(N):
    n = int(input())

    sum_n += n

    max_n = max(n, max_n)
    min_n = min(n, min_n)

    nums[n] += 1
    k = max(k, nums[n])

    h.append(n)

heapq.heapify(h)
for _ in range(N//2):
    heapq.heappop(h)

cnt = 0
mid = 0
for idx in range(-4_000, 4_001):
    if nums[idx] == k:
        cnt += 1
        mid = idx

    if cnt == 2:
        break

print(round(sum_n / N))
print(heapq.heappop(h))
print(mid)
print(max_n - min_n)