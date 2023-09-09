import sys
from collections import deque
sys.stdin = open('input.txt')


def how_long():

    while que:
        now = que.popleft()
        for next, point in graph[now]:
            if next != start_point and (not trace[next] or trace[next] > trace[now] + point):
                que.append(next)
                trace[next] = trace[now] + point



V, E = map(int, input().split())
start_point = int(input())
graph = [[] for _ in range(V+1)]

for _ in range(E):
    now, next, point = map(int, input().split())
    graph[now].append([next, point])

# print(graph)
trace = [0] * (V + 1)
que = deque([start_point])
how_long()
for idx in range(1, V + 1):
    if idx == start_point:
        print(0)
    elif trace[idx]:
        print(trace[idx])
    else:
        print('INF')