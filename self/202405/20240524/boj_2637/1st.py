import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque


N = int(input())
M = int(input())
ing = [0] * (N+1)
weight = [0] * (N+1)
weight[N] = 1
start_point = [True] * (N+1)
reverse = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, c = map(int, input().split())
    start_point[s] = False
    reverse[s].append((e, c))
    ing[e] += 1

q = deque([N])
while q:
    now = q.popleft()
    for next, cost in reverse[now]:
        weight[next] += (weight[now] * cost)
        ing[next] -= 1
        if not ing[next]:
            q.append(next)
# print(weight)
for idx in range(1, N+1):
    if start_point[idx]:
        print(idx, weight[idx])