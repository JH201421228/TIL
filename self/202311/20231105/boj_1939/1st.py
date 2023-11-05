import sys
sys.stdin = open('input.txt')
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    p1, p2, w = map(int, input().split())
    graph[p1].append((p2, -w))
    graph[p2].append((p1, -w))
# for inner in graph:
#     print(inner)
start, end = map(int, input().split())

pq = [(-float('inf'), start)]
visited = [float('inf')] * (N+1)
while pq:
    weight, now = heapq.heappop(pq)
    if now == end:
        print(-weight)
        break
    for next, n_weight in graph[now]:
        if visited[next] <= n_weight:
            continue
        visited[next] = n_weight
        heapq.heappush(pq, (max(weight, n_weight), next))

