import sys
import heapq
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def Thor():
    pq = [(0, S)]
    distance = [float('inf') for _ in range(N)]
    distance[S] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next, weight in graph[now]:
            if not pass_route[now][next]:
                if distance[next] > dist + weight:
                    distance[next] = dist + weight
                    heapq.heappush(pq, (dist + weight, next))
    return distance


def Odin():
    que = deque([D])

    while que:
        now = que.popleft()
        if now == S:
            continue
        for next, weight in graph_inv[now]:
            if distance[next] + weight == distance[now] and not pass_route[next][now]:
                pass_route[next][now] = 1
                que.append(next)


while True:
    N, M = map(int, input().split())
    if not N and not M:
        break
    S, D = map(int, input().split())
    graph = [[] for _ in range(N)]
    graph_inv = [[] for _ in range(N)]
    pass_route = [[0] * N for _ in range(N)]
    for _ in range(M):
        start, end, point = map(int, input().split())
        graph[start].append((end, point))
        graph_inv[end].append((start, point))
    distance = Thor()
    Odin()
    ans = Thor()[D]
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)