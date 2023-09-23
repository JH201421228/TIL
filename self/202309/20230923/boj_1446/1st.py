import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def speed_racer():
    pq = [(0, 0)]
    distance = [float('inf') for _ in range(D+1)]
    distance[0] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next, weight in road[now]:
            if next <= D:
                if distance[next] > weight + dist:
                    distance[next] = weight + dist
                    heapq.heappush(pq, (dist + weight, next))
    return distance[D]


N, D = map(int, input().split())
road = [[(i+1, 1)] for i in range(D+1)]
for _ in range(N):
    start, end, point = map(int, input().split())
    if start <= D:
        road[start].append((end, point))
# print(road)
print(speed_racer())