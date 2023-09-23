import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dua_lipa():
    pq = [(0, 1)]
    distance = [[float('inf')] * k for _ in range(n+1)]
    distance[1][0] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        for next, weight in graph[now]:
            if distance[next][k-1] > dist + weight:
                distance[next][k-1] = dist + weight
                distance[next].sort()
                heapq.heappush(pq, (dist + weight, next))
    return distance



n, m, k = map(int, input().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    start, end, point = map(int, input().split())
    graph[start].append((end, point))
# print(graph)
# print(dua_lipa())
ans_list = dua_lipa()
for idx in range(1, n+1):
    if ans_list[idx][k-1] == float('inf'):
        print(-1)
    else:
        print(ans_list[idx][k-1])
