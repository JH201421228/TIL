import sys
import heapq
sys.stdin = open('input.txt')


def find_hard_route(start):
    distance = [0] * (N+1)
    pq = [(0, start)]

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] > dist:
            continue
        for next, weight in graph[now]:
            next_dist = dist + weight

            if next_dist > distance[next]:
                distance[next] = next_dist
                heapq.heappush(pq, (next_dist, next))
    return distance

T = int(input())
for test in range(T):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        start, end, point = map(int, input().split())
        graph[start].append((end, point))
    # print(graph)
    print(find_hard_route(X))