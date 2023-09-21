import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def let_s_go():
    distance = [float('inf')] * (N+1)
    distance[start] = 0
    pq = [(0, start)]
    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        if now == end:
            break
        for next, weight in graph[now]:
            if distance[next] > dist + weight:
                distance[next] = dist + weight
                heapq.heappush(pq, (dist + weight, next))
    return distance[end]

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, point = map(int, input().split())
    graph[start].append([end, point])
start, end = map(int, input().split())
print(let_s_go())

