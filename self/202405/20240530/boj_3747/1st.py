import sys
sys.stdin = open('input.txt')
from collections import deque
sys.setrecursionlimit(5_000)

def find_scc(now):
    global cnt, order
    parent = visited[now] = order = order + 1
    stack.append(now)

    for nxt in graph[now]:
        if not visited[nxt]:
            parent = min(parent, find_scc(nxt))
        elif not finished[nxt]:
            parent = min(parent, visited[nxt])

    if parent == visited[now]:
        cnt += 1
        while stack:
            out = stack.pop()
            finished[out] = 1
            grp_num[out] = cnt
            if out == now:
                break

    return parent


q = deque([])
input = map(int, sys.stdin.read().split())
while True:
    try:
        a = next(input)
        b = next(input)
        q.append((a, b))
    except:
        break

while q:
    N, M = q.popleft()
    graph = [[] for _ in range(2*N+1)]
    visited = [0] * (2*N+1)
    finished = [0] * (2*N+1)
    order = 0
    cnt = 0
    grp_num = [0] * (2*N+1)
    stack = []
    for _ in range(M):
        a, b = q.popleft()
        if a == b:
            graph[-a].append(a)
        else:
            graph[-a].append(b)
            graph[-b].append(a)

    for idx in range(-N, N+1):
        if idx and not visited[idx]:
            find_scc(idx)
    ans = 1
    for idx in range(1, N+1):
        if grp_num[idx] == grp_num[-idx]:
           ans = 0
           break
    print(ans)