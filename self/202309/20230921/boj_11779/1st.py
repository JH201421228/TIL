import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def ann_marie_birthday(start, end):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0

    pq = [(0, start, str(start))]

    while pq:
        dist, now, log = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        if now == end:
            break
        for next, weight in graph[now]:
            if distance[next] > dist + weight:
                distance[next] = dist + weight
                heapq.heappush(pq, (dist + weight, next, log + str(next)))
                # print(distance)
                # log.append(next)
                # print(log)
    return dist, log


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end, point = map(int, input().split())
    graph[start].append((end, point))
start, end = map(int, input().split())
# log = [start]
ans, log =  ann_marie_birthday(start, end)
# print(log)
print(ans)
print(len(log))
print(*log)