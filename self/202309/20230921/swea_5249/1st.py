import sys
import heapq
sys.stdin = open('input.txt')


def least_tree():
    pq = [(0, 0)]
    distance = [float('inf') for _ in range(V+1)]
    distance[0] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if dist > distance[now]:
            continue
        for next, weight in graph[now]:
            if distance[next] > dist + weight:
                distance[next] = dist + weight
                heapq.heappush(pq, (dist + weight, next))
    return distance



T = int(input())
for test in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2, point = map(int, input().split())
        graph[n1].append((n2, point))
        graph[n2].append((n1, point))
    print(least_tree())
