import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


# 결과가 모든 가수를 포함하고 있지 않으면 0을 출력

N, M = map(int, input().split())
order_list = [[] for _ in range(N+1)]
order_dict = {}
start_point = [True] * (N+1)

for _ in range(M):
    temp = list(map(int, input().split()))
    for idx in range(1, temp[0]):
        order_list[temp[idx]].append(temp[idx+1])
        order_dict[temp[idx+1]] = order_dict.get(temp[idx+1], 0) + 1
        if idx > 1:
            start_point[temp[idx]] = False
    start_point[temp[-1]] = False
# print(start_point, order_list, order_dict)

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
if len(ans) == N:
    for n in ans:
        print(n)
else:
    print(0)