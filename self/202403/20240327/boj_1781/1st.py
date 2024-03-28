import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq


N = int(input())
q = []
for _ in range(N):
    a, b = map(int, input().split())
    heapq.heappush(q, (-b, a))
visited = [0] * (N+1)
path = [i for i in range(N+1)]
print(q)
print(visited)
print(path)
while q:
    b, a = heapq.heappop(q)
    

