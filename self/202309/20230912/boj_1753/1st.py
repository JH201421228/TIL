import sys
from collections import deque
sys.stdin = open('input.txt')


def how_long():

    while que:
        now = que.popleft()
        for next in range(V + 1):
            if next != start_point and graph[now][next] and (not trace[next] or trace[next] > trace[now] + graph[now][next]):
                que.append(next)
                trace[next] = trace[now] + graph[now][next]



V, E = map(int, input().split())
start_point = int(input())
graph = [[0] * (V+1) for _ in range(V+1)]
for _ in range(E):
    now, next, point = map(int, input().split())
    if not graph[now][next] or graph[now][next] > point:
        graph[now][next] = point
        # graph[next][now] = point

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