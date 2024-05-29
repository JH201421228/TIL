import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(100_000)
from collections import deque


def find_scc(now):
    order_list.append(now)
    order[0] += 1
    parent = visited[now] = order[0]
    stack.append(now)

    for next in graph[now]:
        if not visited[next]:
            parent = min(parent, find_scc(next))
        elif not finished[next]:
            parent = min(parent, visited[next])

    if parent == visited[now]:
        temp = []
        while stack:
            out = stack.pop()
            finished[out] = 1
            temp.append(abs(out))
            if now == out:
                ans.append(temp)
                break

    return parent


N, M = map(int, input().split())
graph = [[] for _ in range(2*N+1)]
finished = [0] * (2*N + 1)
visited = [0] * (2*N + 1)
order = [0]
stack = []
ans = []
order_list = deque([])

for _ in range(M):
    p1, p2 = map(int, input().split())
    graph[p1].append(-p2)
    graph[p2].append(-p1)

for idx in range(-N, N+1):
    if idx and not visited[idx]:
        find_scc(idx)

for inner in ans:
    inner_set = set(inner)
    for n in inner:
        if len(inner_set) != len(inner):
            print(0)
            print(visited)
            print(ans)
            print(order_list)
            exit(0)
print(1)
print(visited)
print(order_list)
print(ans)