import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


N = int(input())
M = int(input())

# order_list = [[] for _ in range(N+1)]
# reverse = [[] for _ in range(N+1)]
graph = [[0] * (N+1) for _ in range(N+1)]
order_dict = {}
road_cost = {}

weight = [0] * (N+1)

for _ in range(M):
    s, e, c = map(int, input().split())
    # order_list[s].append(e)
    # reverse[e].append(s)
    road_cost[(s, e)] = c
    order_dict[e] = order_dict.get(e, 0) + 1
    graph[s][e] = 1

start, end = map(int, input().split())
# print(order_dict, order_list, road_cost, start, end)

q = deque([start])

while q:
    now = q.popleft()
    for next in range(1, N+1):
        if graph[now][next]:
            weight[next] = max(weight[next], weight[now] + road_cost[(now, next)])
            order_dict[next] -= 1
            if not order_dict[next]:
                q.append(next)
print(weight[end])
# print(weight)

ans = 0
# ans_list = set()
q = deque([end])
while q:
    now = q.popleft()
    for next in range(1, N+1):
        if graph[next][now]:
            if weight[now] - road_cost[(next, now)] == weight[next]:
                ans += 1
                # ans_list.add((next, now))
                graph[next][now] = 0
                # print(now, next)
                q.append(next)
# print(ans)
# print(len(ans_list))
print(ans)