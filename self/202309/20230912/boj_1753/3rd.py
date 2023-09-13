import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

def how_cost():
    while que:
        cost, now = que.popleft()
        if trace[now] < cost:
            continue
        for next, next_cost in graph[now]:
            new_cost = cost + next_cost
            if new_cost < trace[next]:
                trace[next] = next_cost
                que.append([new_cost, next])


V, E = map(int, input().split())
start_point = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    now, next, point = map(int, input().split())
    graph[now].append([next, point])
que = deque([[0, start_point]])
trace = [float('inf')] * (V + 1)
trace[start_point] = 0
# print(graph)
how_cost()
for idx in range(1, V + 1):
    if idx == start_point:
        print(0)
    elif trace[idx] == float('inf'):
        print('INF')
    else:
        print(trace[idx])