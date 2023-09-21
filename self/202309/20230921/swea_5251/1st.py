import sys
import heapq
sys.stdin = open('input.txt')


def swea_5251():
    distance = [float('inf')] * (N + 1)
    distance[0] = 0
    pq = [(0, 0)]

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        if now == N:
            break
        for next, weight in graph[now]:
            if distance[next] > dist + weight:
                distance[next] = dist + weight
                heapq.heappush(pq, (dist + weight, next))
    return dist


T = int(input())
for test in range(T):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        start, end, point = map(int, input().split())
        graph[start].append((end, point))
    print(f'#{test + 1} {swea_5251()}')
