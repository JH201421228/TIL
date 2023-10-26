import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def tired(start, end):
    distance = [0] * (N+1)
    pq = [(0, start)]
    while pq:
        dist, now = heapq.heappop(pq)
        dist *= -1

        if now == end:
            print(dist)
            return

        if distance[now] > dist:
            continue

        for n_dist, next in graph[now]:
            if not dist:
                distance[next] = n_dist
                heapq.heappush(pq, )


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
    graph[B].append((C, A))

for i in range(1, N+1):
    graph[i].sort(reverse=True)