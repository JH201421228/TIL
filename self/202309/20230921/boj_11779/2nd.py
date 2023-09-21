import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def ann_marie_birthday(start, end):
    distance = [[float('inf'), 0] for _ in range(n + 1)]
    distance[start][0] = 0

    pq = [(0, start)]

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now][0] < dist:
            continue
        if now == end:
            break
        for next, weight in graph[now]:
            if distance[next][0] > dist + weight:
                distance[next][0] = dist + weight
                distance[next][1] = now
                heapq.heappush(pq, (dist + weight, next))
                # print(distance)
                # log.append(next)
                # print(log)
    return dist, distance


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end, point = map(int, input().split())
    graph[start].append((end, point))
start, end = map(int, input().split())

ans, log = ann_marie_birthday(start, end)
print(ans)
print(log)
# while True:
