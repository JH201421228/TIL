import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dijkstra(start):
    pq = [(0, start, 0)]
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    kth_shortest_distances = [[] for _ in range(n + 1)]

    while pq:
        dist, now, cnt = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        if len(kth_shortest_distances[now]) < k:
            kth_shortest_distances[now].append(dist)

        if cnt == k - 1:
            continue

        for next, weight in graph[now]:
            if dist + weight < distance[next]:
                distance[next] = dist + weight
                heapq.heappush(pq, (dist + weight, next, cnt + 1))

    return kth_shortest_distances

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, point = map(int, input().split())
    graph[start].append((end, point))

kth_shortest_distances = dijkstra(1)

for i in range(1, n + 1):
    if len(kth_shortest_distances[i]) == k:
        print(kth_shortest_distances[i][-1])
    else:
        print(-1)
