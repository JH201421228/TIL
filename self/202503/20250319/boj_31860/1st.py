import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M, K = map(int, input().split())

q = []
for _ in range(N):
    heapq.heappush(q, -int(input()))

satisfaction = [0]

while q:
    n = -heapq.heappop(q)
    satisfaction.append(satisfaction[-1]//2 + n)

    if n-M > K:
        heapq.heappush(q, -n+M)

print(len(satisfaction)-1)
for idx in range(1, len(satisfaction)):
    print(satisfaction[idx])