import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def fox_run():
    pq = [(0, 1)]
    distance = [float('inf')] * (N+1)
    distance[1] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next, weight in graph[now]:
            if distance[next] > dist + weight:
                distance[next] = dist + weight
                heapq.heappush(pq, (dist + weight, next))
    return distance

def wolf_run():
    pq = [(0, 0.5, 1)]
    distance = [float('inf')] * (N + 1)
    distance[1] = 0

    while pq:
        dist, status, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next, weight in graph[now]:
            if distance[next] > dist + weight * status:
                distance[next] = dist + weight * status
                heapq.heappush(pq, (dist + weight * status, 1/status, next))
    return distance

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    p1, p2, point = map(int, input().split())
    graph[p1].append((p2, point))
    graph[p2].append((p1, point))
print(fox_run())
print(wolf_run())