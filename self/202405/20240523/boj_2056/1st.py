import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


N = int(input())
order_list = [[] for _ in range(N+1)]
order_dict = {}
cost = [0]
weight = [0] * (N+1)

q = deque([])

for idx in range(1, N+1):
    temp = list(map(int, input().split()))
    cost.append(temp[0])

    if not temp[1]:
        q.append(idx)
    else:
        order_dict[idx] = temp[1]
    for i in range(2, 2+temp[1]):
        order_list[temp[i]].append(idx)

# print(order_dict, order_list, cost, q)

while q:
    now = q.popleft()
    for next in order_list[now]:
        order_dict[next] = order_dict.get(next) - 1
        weight[next] = max(weight[next], weight[now] + cost[now])
        if not order_dict[next]:
            q.append(next)

ans = 0
for idx in range(1, N+1):
    ans = max(weight[idx] + cost[idx], ans)
print(ans)