import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())
order_dict = {}
order_list = [[] for _ in range(N+1)]
start_point = [True] * (N+1)

for _ in range(M):
    s, e = map(int, input().split())
    order_list[s].append(e)
    start_point[e] = False
    order_dict[e] = order_dict.get(e, 0) + 1

q = deque([])
for idx in range(1, N+1):
    if start_point[idx]:
        q.append(idx)

ans = []
while q:
    now = q.popleft()
    for next in order_list[now]:
        order_dict[next] = order_dict.get(next) - 1
        if not order_dict[next]:
            q.append(next)
    ans.append(now)

print(*ans)