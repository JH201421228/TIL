import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline


def why_play_this_game(start):
    pq = [(0, start)]
    distance = [float('inf') for _ in range(n+1)]
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue
        for next, weight in graph[now]:
            if distance[next] > dist + weight:
                distance[next] = dist + weight
                heapq.heappush(pq, (dist + weight, next))
    return distance


n, m, r = map(int, input().split())
item_list = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(r):
    start, end, point = map(int, input().split())
    graph[start].append((end, point))
    graph[end].append((start, point))
value = 0
for idx in range(1, n+1):
    ans = 0
    ans_list = why_play_this_game(idx)[1:]
    for idx in range(n):
        if ans_list[idx] <= m:
            ans += item_list[idx]
    if ans > value:
        value = ans
print(value)