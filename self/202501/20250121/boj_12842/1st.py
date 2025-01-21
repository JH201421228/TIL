import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, S = map(int, input().split())
M = int(input())

B = [int(input()) for _ in range(M)]

q = []
for i in range(M):
    q.append((0, i))

ans = 0

while True:
    d, n = heapq.heappop(q)
    ans += 1

    if ans == N-S:
        print(n+1)
        break

    q.append((d+B[n], n))