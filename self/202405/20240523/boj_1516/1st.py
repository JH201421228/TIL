import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


N = int(input())
cost = [0]
order_dict = {}
order_list = [[] for _ in range(N+1)]
q = deque([])
weight = [0] * (N+1)

for idx in range(1, N+1):
    temp = list(map(int, input().split()))
    cost.append(temp[0])
    if temp[1] == -1:
        q.append(idx)
    else:
        for n in temp[1:len(temp)-1]:
            order_list[n].append(idx)
            order_dict[idx] = order_dict.get(idx, 0) + 1

# print(order_list, order_dict, q)

while q:
    now = q.popleft()
    for next in order_list[now]:
        weight[next] = max(weight[next], weight[now] + cost[now])
        order_dict[next] = order_dict.get(next) - 1
        if not order_dict[next]:
            q.append(next)

for idx in range(1, N+1):
    print(weight[idx] + cost[idx])