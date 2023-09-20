import sys
import heapq

sys.stdin = open('input.txt')

def find_longest_distance(start):
    distance = [-float('inf')] * (N + 1)
    pq = [(0, start)]

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] > dist:
            continue
        for next_node, weight in graph[now]:
            next_dist = dist + weight

            if next_dist > distance[next_node]:
                distance[next_node] = next_dist
                heapq.heappush(pq, (next_dist, next_node))

    return distance

T = int(input())
for test in range(T):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        start, end, point = map(int, input().split())
        graph[start].append((end, point))
    result = find_longest_distance(X)
    max_distance = max(result[1:])
    if max_distance == -float('inf'):
        print("Impossible")  # 최장 거리가 음의 무한대이면 도달할 수 없음
    else:
        print(max_distance)
