import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def holiday(start):
    pq = [(0, start)]
    distance = [float('inf')] * (V+1)
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next, weight in graph[now]:
            if distance[next] > dist+weight:
                distance[next] = dist+weight
                heapq.heappush(pq, (dist+weight, next))
    return distance


V, E, P = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    p1, p2, point = map(int, input().split())
    graph[p1].append((p2, point))
    graph[p2].append((p1, point))
ans1 = holiday(1)
ans2 = holiday(P)
if ans1[V] == ans2[1] + ans2[V]:
    print('SAVE HIM')
else:
    print('GOOD BYE')
