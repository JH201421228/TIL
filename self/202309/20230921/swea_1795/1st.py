import sys
import heapq
sys.stdin = open('input.txt')


def house_party_protocol1(node):
    distance = [float('inf') for _ in range(N+1)]
    distance[0] = distance[node] = 0
    pq = [(0, node)]

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next, weight in graph1[now]:
            if distance[next] > dist + weight:
                distance[next] = dist + weight
                heapq.heappush(pq, (dist + weight, next))
    return distance


def house_party_protocol2(node):
    distance = [float('inf') for _ in range(N + 1)]
    distance[0] = distance[node] = 0
    pq = [(0, node)]

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next, weight in graph2[now]:
            if distance[next] > dist + weight:
                distance[next] = dist + weight
                heapq.heappush(pq, (dist + weight, next))
    return distance


T = int(input())
for test in range(T):
    N, M, X = map(int, input().split())
    graph1 = [[] for _ in range(N + 1)]
    graph2 = [[] for _ in range(N + 1)]
    for _ in range(M):
        start, end, point = map(int, input().split())
        graph1[start].append((end, point))
        graph2[end].append((start, point))
    ans1 = house_party_protocol1(X)
    ans2 = house_party_protocol2(X)
    ans = 0
    for idx in range(1, N+1):
        if idx == X:
            continue
        if ans < ans1[idx] + ans2[idx]:
            ans = ans1[idx] + ans2[idx]
    print(f'#{test+1} {ans}')


