import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

def holiday():
    pq = [(0, 0)]
    distance = [float('inf')] * N
    distance[0] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next, weight in graph[now]:
            if not watch[next] or next == N-1:
                if distance[next] > dist + weight:
                    distance[next] = dist + weight
                    heapq.heappush(pq, (dist+weight, next))
    return distance[N-1]


N, M = map(int, input().split())
watch = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    p1, p2, point = map(int, input().split())
    graph[p1].append((p2, point))
    graph[p2].append((p1, point))
# 시야에 보이지 않으면서 최단경로 추적
ans = holiday()
if ans == float('inf'):
    print(-1)
else:
    print(ans)