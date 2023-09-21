import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def ann_marie_birthday(start, end):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    path = [0] * (n+1)

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
                path[next] = now
                heapq.heappush(pq, (dist + weight, next))
                # print(distance)
                # log.append(next)
                # print(log)
    return dist, path


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end, point = map(int, input().split())
    graph[start].append((end, point))
start, end = map(int, input().split())
# log = [start]
ans, path = ann_marie_birthday(start, end)
# print(log)
print(ans)
# print(path)
ans_list = [end]
while True:
    if end == start:
        break
    ans_list.insert(0, path[end])
    end = path[end]

print(len(ans_list))
print(*ans_list)
