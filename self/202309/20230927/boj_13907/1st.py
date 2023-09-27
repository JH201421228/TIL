import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def for_test(t):
    pq = [(0, S)]
    distance = [float('inf') for _ in range(N+1)]
    distance[S] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        if now == D:
            return dist
        for next, weight in graph[now]:
            if distance[next] > dist + weight + t:
                distance[next] = dist + weight + t
                heapq.heappush(pq, (dist + weight + t, next))
    return distance[D]


N, M, K = map(int, input().split())
S, D = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))
    graph[end].append((start, weight))
taxs = []
for _ in range(K):
    taxs.append(int(input()))
print(for_test(0))
tax = 0
for tax_add in taxs:
    tax += tax_add
    print(for_test(tax))
