import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dua_lipa():
    pq = [(0, 1, 0)]
    distance = [float('inf') for _ in range(n+1)]
    distance[1] = 0
    check_list = [0] * (n+1)

    while pq:
        dist, now, cnt = heapq.heappop(pq)
        if cnt == k:
            check_list[now] = dist
            continue
        for next, weight in graph[now]:
            distance[next] = dist + weight
            heapq.heappush(pq, (dist + weight, next, cnt + 1))
    return check_list


n, m, k = map(int, input().split())
graph = [[] for i in range(n+1)]
for _ in range(m):
    start, end, point = map(int, input().split())
    graph[start].append((end, point))
# print(graph)
print(dua_lipa())
