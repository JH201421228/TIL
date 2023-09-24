import sys
import heapq
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def good_day():
    pq = [(0, 1)]
    distance = [float('inf') for _ in range(N+1)]
    distance[1] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next, weight in graph[now]:
            if distance[next] > dist + weight:
                distance[next] = dist + weight
                heapq.heappush(pq, (dist + weight, next))
                route[next] = now


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    p1, p2, point = map(int, input().split())
    graph[p1].append((p2, point))
    graph[p2].append((p1, point))
# 1번 노드에서 다른 노드에 도달하는 거리가 최소, 가중치 합도 최소

# print(distance)
route = [0] * (N+1)
good_day()
# print(route)
print(N-1)
for i in range(2, N+1):
    print(i, route[i])
