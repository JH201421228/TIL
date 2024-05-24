import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


def dfs(now, val, goal, arr):
    if val == goal:
        ans.append(arr)
        return
    if val > weight[now]:
        return
    for next in order_list[now]:
        dfs(next, val+road_cost[(now, next)], goal, arr+[next])


N = int(input())
M = int(input())

order_list = [[] for _ in range(N+1)]
order_dict = {}
road_cost = {}

weight = [0] * (N+1)

for _ in range(M):
    s, e, c = map(int, input().split())
    order_list[s].append(e)
    road_cost[(s, e)] = c
    order_dict[e] = order_dict.get(e, 0) + 1

start, end = map(int, input().split())
# print(order_dict, order_list, road_cost, start, end)

q = deque([start])

while q:
    now = q.popleft()
    for next in order_list[now]:
        # if weight[now] + road_cost[(now, next)] > weight[next]:
        #     weight[next] = weight[now] + road_cost[(now, next)]
        #     long[next] = long[now].union({(now, next)})
        # elif weight[now] + road_cost[(now, next)] == weight[next]:
        #     long[next] = long[next].union(long[now].union({(now, next)}))
        weight[next] = max(weight[next], weight[now] + road_cost[(now, next)])
        order_dict[next] -= 1
        if not order_dict[next]:
            q.append(next)
print(weight[end])
ans = []
dfs(start, 0, weight[end], [start])
# print(ans)
ans_set = set()
for inner in ans:
    for idx in range(len(inner)-1):
        ans_set.add((inner[idx], inner[idx+1]))
print(len(ans_set))