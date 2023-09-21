import sys
import heapq
sys.stdin = open('input.txt')

def prim_mst():
    pq = [(0, 0)]  # 우선순위 큐를 사용한 프림 알고리즘 구현
    visited = [False] * (V+1)
    distance = [float('inf')] * (V+1)
    distance[0] = 0
    ans = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if visited[now]:
            continue
        visited[now] = True
        ans += dist

        for next, weight in graph[now]:
            if not visited[next] and distance[next] > weight:
                distance[next] = weight
                heapq.heappush(pq, (weight, next))

    return ans

T = int(input())
for test in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2, point = map(int, input().split())
        graph[n1].append((n2, point))
        graph[n2].append((n1, point))
    print(prim_mst())
