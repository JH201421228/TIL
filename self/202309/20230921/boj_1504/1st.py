import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

def is_it_okay(start, end):
    pq = [(0, start)]
    distance = [float('inf')] * (N+1)
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        if now == end:
            break
        for next, weight in graph[now]:
            if distance[next] > dist + weight:
                distance[next] = dist + weight
                heapq.heappush(pq, (dist + weight, next))
    return distance[end]


N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    start, end, point = map(int, input().split())
    graph[start].append((end, point))
    graph[end].append((start, point))
v1, v2 = map(int, input().split())
# print(is_it_okay(1, v1))
# print(is_it_okay(1, v2))
# print(is_it_okay(v2, end))
# print(is_it_okay(v1, end))
ans = min(is_it_okay(1, v1) + is_it_okay(v2, N), is_it_okay(1, v2) + is_it_okay(v1, N)) + is_it_okay(v1, v2)
if ans == float('inf'):
    print(-1)
else:
    print(ans)
# print(is_it_okay(v1, v2), is_it_okay(v2, v1))
