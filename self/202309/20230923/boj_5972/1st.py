import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def Cow_Boy():
    pq = [(0, 1)]
    distance = [float('inf') for _ in range(N+1)]
    distance[1] = 0
    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next, weiht in graph[now]:
            if distance[next] > dist + weiht:
                distance[next] = dist + weiht
                heapq.heappush(pq, (dist + weiht, next))
    return distance[N]

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    p1, p2, point = map(int, input().split())
    graph[p1].append((p2, point))
    graph[p2].append((p1, point))
print(Cow_Boy())
